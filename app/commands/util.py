from app.util.imports import import_handler

def group_commands(group, commands):
    for command in commands:
        path    = "{path}.command".format(path = command)
        command = import_handler(path)
        
        group.add_command(command)
    
    return group