.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: format
format:  ## 🔧 코드를 포매팅합니다.
	pycln .
	black .
	isort .

.PHONY: test
test:  ## 🧪 테스트 코드를 실행합니다.
	pytest tests/

.PHONY: run
run:  ## run application
	python CRUD/main.py


.PHONY: clean
clean:
	find . -type f -name "*.pyc" | xargs rm -fr
	find . -type d -name __pycache__ |xargs rm -fr