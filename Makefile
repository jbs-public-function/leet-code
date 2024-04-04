clean-repos:
	git branch | grep -vE "(main)" | xargs git branch -D

clean-tests:
	python -m black tests

clean-leet-codes:
	python -m black leet_code

run-tests:
	python -m pytest tests
