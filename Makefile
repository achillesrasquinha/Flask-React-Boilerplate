BASEDIR					= $(shell pwd)
-include ${BASEDIR}/.env

APP_ENVIRONMENT			= development

PROJECT					= app

PROJDIR					= ${BASEDIR}/${PROJECT}

PYTHONPATH		 	   ?= $(shell command -v python)
VIRTUALENV				= $(shell command -v virtualenv)

VENVDIR				   ?= ${BASEDIR}/.venv
VENVBIN					= ${VENVDIR}/bin

PYTHON				  	= ${VENVBIN}/python
PIP					  	= ${VENVBIN}/pip
PYTEST				  	= ${VENVBIN}/pytest
PYLINT					= ${VENVBIN}/pylint
IPYTHON					= ${VENVBIN}/ipython

YARN				    = $(shell command -v yarn)

JOBS				   ?= $(shell $(PYTHONPATH) -c "import multiprocessing as mp; print(mp.cpu_count())")

define log
	$(eval CLEAR     = \033[0m)
	$(eval BOLD		 = \033[0;1m)
	$(eval INFO	     = \033[0;36m)
	$(eval SUCCESS   = \033[0;32m)

	$(eval BULLET 	 = "→")
	$(eval TIMESTAMP = $(shell date +%H:%M:%S))

	@echo "${BULLET} ${$1}[${TIMESTAMP}]${CLEAR} ${BOLD}$2${CLEAR}"
endef

ifndef VERBOSE
.SILENT:
endif

install: clean
	$(call log,INFO,Building Python Requirements)
	cat $(BASEDIR)/requirements/*.txt 		   > $(BASEDIR)/requirements-dev.txt
	cat $(BASEDIR)/requirements/production.txt > $(BASEDIR)/requirements.txt

	$(call log,INFO,Installing Python Requirements)
	$(PIP) install -r $(BASEDIR)/requirements-dev.txt

	$(call log,INFO,Installing ${PROJECT} (${APP_ENVIRONMENT}))
ifeq (${APP_ENVIRONMENT},development)
	$(PYTHON) setup.py develop
else
	$(PYTHON) setup.py install
endif

	$(call log,INFO,Installing Node Requirements)

	$(YARN)

	$(call log,SUCCESS,Installation Successful)


clean:
	clear

	$(call log,INFO,Cleaning Python Cache)
	find $(BASEDIR) | grep -E "__pycache__|\.pyc" | xargs rm -rf

	rm -rf \
		$(BASEDIR)/*.egg-info \
		$(BASEDIR)/.pytest_cache \
		$(BASEDIR)/.coverage \
		$(BASEDIR)/htmlcov

	$(call log,SUCCESS,Cleaning Successful)

test: install
	$(call log,INFO,Running Python Tests using $(JOBS) jobs.)

ifeq (${TEST_FAIL},true)
	$(eval FAIL := -x)
endif

	$(PYTEST) -n $(JOBS) $(FAIL) --cov=$(PROJDIR) --cov-report html $(ARGS)
	open $(BASEDIR)/htmlcov/index.html
	
	$(call log,SUCCESS,Python Tests Successful)

env:
	$(call log,INFO,Creating a Virtual Environment ${VENVDIR} with Python - ${PYTHONPATH})
	$(VIRTUALENV) $(VENVDIR) -p $(PYTHONPATH)

console: install
	$(call log,INFO,Launching Python Console)
	$(IPYTHON) \
		--no-banner