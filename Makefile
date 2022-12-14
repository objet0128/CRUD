.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: format
format:  ## ๐ง ์ฝ๋๋ฅผ ํฌ๋งคํํฉ๋๋ค.
	pycln .
	black .
	isort .

.PHONY: test
test:  ## ๐งช ํ์คํธ ์ฝ๋๋ฅผ ์คํํฉ๋๋ค.
	pytest tests/

.PHONY: run
run:  ## run application
	python CRUD/main.py


.PHONY: clean
clean:
	find . -type f -name "*.pyc" | xargs rm -fr
	find . -type d -name __pycache__ |xargs rm -fr


.PHONY: setup
setup: ## setup application
	poetry install
	poetry shell
	pre-commit install