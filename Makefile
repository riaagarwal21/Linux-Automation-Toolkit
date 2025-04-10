# Makefile for Linux System Automation Toolkit

.PHONY: help run test coverage clean

# Run the CLI toolkit
run:
	python3 toolkit.py --help

# Run all tests using pytest
test:
	pytest tests/

# Run tests with coverage and generate HTML report
coverage:
	pytest --cov=modules tests/ --cov-report term --cov-report html

# Open the HTML coverage report (Linux GUI systems)
coverage-view:
	chromium-browser htmlcov/index.html

# Clean up cache and coverage files
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf .pytest_cache
	rm -rf htmlcov
