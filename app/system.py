# imports - standard imports
import os
import os.path as osp
import subprocess
from   distutils.spawn import find_executable

# imports - module imports
import app

def pardir(fname, level = 1):
    for _ in range(level):
        fname = osp.dirname(fname)
    return fname

def which(exec_, raise_err = False):
    executable = find_executable(exec_)
    if not executable and raise_err:
        raise app.ValueError("{executable} executable not found.".format(
            executable = exec_
        ))
    
    return executable

def popen(*args, **kwargs):
    output      = kwargs.get("output", False)
    directory   = kwargs.get("cwd")
    environment = kwargs.get("env")
    shell       = kwargs.get("shell", True)
    raise_err   = kwargs.get("raise_err", True)

    environ     = os.environ.copy()
    if environment:
        environ.update(environment)

    for k, v in environ.items():
        environ[k] = str(v)

    command     = " ".join([str(arg) for arg in args])
    app.log.info("Running command: {command} with environment variables: {variables}".format(
        command   = command,
        variables = environment
    ))
    
    proc        = subprocess.Popen(command,
        stdin   = subprocess.PIPE if output else None,
        stdout  = subprocess.PIPE if output else None,
        stderr  = subprocess.PIPE if output else None,
        env     = environ,
        cwd     = directory,
        shell   = shell
    )

    code       = proc.wait()

    if code and raise_err:
        raise subprocess.CalledProcessError(code, command)

    if output:
        output, error = proc.communicate()

        if output:
            output = output.decode("utf-8")
            output = strip(output)

        if error:
            error  = error.decode("utf-8")
            error  = strip(error)

        return code, output, error
    else:
        return code