install-local:
	pip3 install twine
	rm omni-coveragereporter-python/dist/*.gz
	cd omni-coveragereporter-python && pip3 uninstall omni_coveragereporter
	cd omni-coveragereporter-python && python3 setup.py sdist
	cd omni-coveragereporter-python && pip3 install dist/omni_coveragereporter-0.0.3.tar.gz
release: install-local
	cd omni-coveragereporter-python && twine upload dist/*
