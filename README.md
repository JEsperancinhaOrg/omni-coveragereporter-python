# omni-coveragereporter-python

[![Twitter URL](https://img.shields.io/twitter/url?logoColor=blue&style=social&url=https%3A%2F%2Fimg.shields.io%2Ftwitter%2Furl%3Fstyle%3Dsocial)](https://twitter.com/intent/tweet?text=%20Checkout%20this%20%40github%20repo%20by%20%40joaofse%20%F0%9F%91%A8%F0%9F%8F%BD%E2%80%8D%F0%9F%92%BB%3A%20https%3A//github.com/JEsperancinhaOrg/omni-coveragereporter-python)
[![Generic badge](https://img.shields.io/static/v1.svg?label=GitHub&message=omni-coveragereporter-python&color=informational)](https://github.com/JEsperancinhaOrg/omni-coveragereporter-python)
[![GitHub release](https://img.shields.io/github/release-pre/jesperancinhaorg/omni-coveragereporter-python.svg)](https://github.com/jesperancinhaorg/omni-coveragereporter-python/releases)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/jesperancinhaorg/omni-coveragereporter-python)](https://github.com/jesperancinhaorg/omni-coveragereporter-python/releases)

[![omni-coveragereporter-python](https://github.com/JEsperancinhaOrg/omni-coveragereporter-python/actions/workflows/python-package-pull-request.yml/badge.svg)](https://github.com/JEsperancinhaOrg/omni-coveragereporter-python/actions/workflows/python-package-pull-request.yml)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/f25fb0adabc74f129271fed966b6e8fa)](https://www.codacy.com/gh/JEsperancinhaOrg/omni-coveragereporter-python/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=JEsperancinhaOrg/omni-coveragereporter-python&amp;utm_campaign=Badge_Grade)

[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/f25fb0adabc74f129271fed966b6e8fa)](https://www.codacy.com/gh/JEsperancinhaOrg/omni-coveragereporter-python/dashboard?utm_source=github.com&utm_medium=referral&utm_content=JEsperancinhaOrg/omni-coveragereporter-python&utm_campaign=Badge_Coverage)
[![Coverage Status](https://coveralls.io/repos/github/JEsperancinhaOrg/omni-coveragereporter-python/badge.svg?branch=main)](https://coveralls.io/github/JEsperancinhaOrg/omni-coveragereporter-python?branch=main)
[![codecov](https://codecov.io/gh/JEsperancinhaOrg/omni-coveragereporter-python/branch/main/graph/badge.svg?token=NBlnQ2Qb1D)](https://codecov.io/gh/JEsperancinhaOrg/omni-coveragereporter-python)

## Run Locally

```shell
python3 omni_coveragereporter_python.py
```

## Run Coverage

```shell
coverage run --source=omni-coveragereporter-python -m pytest

coverage report -m

coverage html
coverage json
coverage xml
```

---

## Python packaging commands

```bash
pip3 install twine

cd omni-coveragereporter-python

python3 setup.py sdist

pip3 install dist/omni_coveragereporter-0.0.0.tar.gz

pip3 uninstall omni_coveragereporter

twine upload dist/*
```

---

## Install/Uninstall Python libraries

```bash
sudo pip uninstall omni_coveragereporter

sudo pip install omni_coveragereporter
```

---

## References

- [Codecov Report Upload](https://docs.codecov.com/reference/upload)
- [Codacy Coverage Reporter](https://github.com/codacy/codacy-coverage-reporter)
- [Jackson Module](https://medium.com/@foxjstephen/how-to-actually-parse-xml-in-java-kotlin-221a9309e6e8)
- [XCode Environment Variable Reference](https://developer.apple.com/documentation/xcode/environment-variable-reference)
- [Cross-CI reference](https://github.com/streamich/cross-ci)
- [Coveralls API reference](https://docs.coveralls.io/api-reference)
- [Git Hub Environment Variables](https://docs.github.com/en/actions/learn-github-actions/environment-variables)
- [Git Lab Environment Variables](https://docs.gitlab.com/ee/ci/variables/predefined_variables.html)
- [Check Run Reporter](https://github.com/marketplace/check-run-reporter)
- [Codacy Maven Plugin](https://github.com/halkeye/codacy-maven-plugin)
- [Coveralls Maven Plugin](https://github.com/trautonen/coveralls-maven-plugin)
- [Example Java Maven for CodeCov](https://github.com/codecov/example-java-maven)
- [CodeCov Maven Plugin](https://github.com/alexengrig/codecov-maven-plugin)
