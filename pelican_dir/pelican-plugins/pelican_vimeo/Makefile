.PHONY: install uninstall pypi
install:
	python setup.py install

uninstall:
	pip uninstall pelican_vimeo

pypi:
	python setup.py sdist upload
	python setup.py bdist_egg upload
	python setup.py bdist_wheel upload
