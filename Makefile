init:
	pip install -r requirements.txt

test:
	nosetests tests

docs:
	cd ./docs
	make html

readme:
	pandoc README.md -s -o README.rst

version:
	./update_version.py

publish:
	python setup.py sdist
	python setup.py sdist upload


