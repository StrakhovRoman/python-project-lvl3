install:
	poetry install

	
page-loader:
	@poetry run page-loader


build:
	poetry build


package-install:
	pip install --user dist/*.whl


lint:
	poetry run flake8 page_loader


test:
	poetry run pytest tests -vv


coverage:
	poetry run pytest --cov=page-loader --cov-report xml tests/