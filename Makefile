.DEFAULT_GOAL := build
.PHONY: build publish package coverage test lint docs venv activate
PROJ_SLUG = djio_arcpy
CLI_NAME = djio_arcpy

GREEN = 2
RED = 1
WHITE = 7

define colorecho
        @tput bold
        @tput setaf $1
        @echo $2
        @tput sgr0
endef


build:
	pip install --editable .

run:
	$(CLI_NAME) run

submit:
	$(CLI_NAME) submit

freeze:
	pip freeze > requirements.txt

lint:
	pylint $(PROJ_SLUG)

test: lint
	py.test --cov-report term --cov=$(PROJ_SLUG) tests/

quicktest:
	py.test --cov-report term --cov=$(PROJ_SLUG) tests/

coverage: lint
	py.test --cov-report html --cov=$(PROJ_SLUG) tests/

docs: coverage
	mkdir -p docs/source/_static
	mkdir -p docs/source/_templates
	cd docs && $(MAKE) html

answers:
	cd docs && $(MAKE) html
	cmd /c start docs/build/html/index.html

package: clean docs
	python setup.py sdist

publish: package
	twine upload dist/*

clean :
	rm -rf dist \
	rm -rf docs/build \
	rm -rf *.egg-info
	coverage erase

venv :
	conda create --clone arcgispro-py3 --name djio-arcpy
	@echo To activate the environment, use the following command:
	$(call colorecho, $(GREEN), "activate djio-arcpy")
	@echo
	$(call colorecho, $(WHITE), "Once activated you can use the 'install' to gather dependencies.")
	@echo
	$(call colorecho, $(GREEN), "source venv/bin/activate")

activate:
	@echo make cannot do this for you, but you can activate the project environment with the following command:
	@echo
	$(call colorecho, $(GREEN), "activate djio-arcpy")	

install:
	pip install -r requirements.txt

licenses:
	pip-licenses --with-url --format-rst \
	--ignore-packages $(shell cat .pip-license-ignore | awk '{$$1=$$1};1')
