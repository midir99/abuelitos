#! /usr/bin/make
#
# Makefile for Abuelitos project.
#
# Targets:
# - "clean" removes directories created by Python and development tools.
# - "format" formats the Python code and sorts the imports.
# - "lint" lints the Python code.
# - "test" tests the Python code.


clean:
	find . -name '__pycache__' | xargs rm -rf
	rm -rf htmlcov .coverage .pytest_cache


format:
	python3 -m black .
	python3 -m isort .
	python3 -m autoflake --remove-all-unused-imports -i -r .


lint:
	python3 -m pylint .


test:
	python3 -m pytest
