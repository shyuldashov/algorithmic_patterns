DIRS = design_gurus
VALIDATORS = flake8 pylint mypy

dev-pep8:
	isort $(DIRS);
	black $(DIRS);

dev-pep8-check:
	for validator in $(VALIDATORS); do \
		echo "\nChecking $$validator"; \
		$$validator $(DIRS); \
	done;
