default: unit
.PHONY: unit
unit:
	@nosetests -v
init:
	pip install -r requirements.txt
