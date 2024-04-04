clean-repos:
	git branch | grep -vE "(main)" | xargs git branch -D

