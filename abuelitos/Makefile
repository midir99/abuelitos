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
	python3 -m black abuelitos
	python3 -m isort abuelitos


lint:
	python3 -m pylint abuelitos


test:
	python3 -m pytest
