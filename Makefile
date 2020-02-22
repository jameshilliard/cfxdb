clean:
	-rm -rf ./.pytest_cache
	-rm -rf ./build
	-rm -rf ./dist
	-rm -rf ./*.egg-info
	-find . -type d -name "__pycache__" -exec rm -rf {} \;

install:
	pip install -e .

publish: clean
	python setup.py sdist bdist_wheel --universal
	twine upload dist/*
