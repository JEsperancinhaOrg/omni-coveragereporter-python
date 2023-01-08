# omni-coveragereporter-python

[![Twitter URL](https://img.shields.io/twitter/url?logoColor=blue&style=social&url=https%3A%2F%2Fimg.shields.io%2Ftwitter%2Furl%3Fstyle%3Dsocial)](https://twitter.com/intent/tweet?text=%20Checkout%20this%20%40github%20repo%20by%20%40joaofse%20%F0%9F%91%A8%F0%9F%8F%BD%E2%80%8D%F0%9F%92%BB%3A%20https%3A//github.com/JEsperancinhaOrg/omni-coveragereporter-python)
[![Generic badge](https://img.shields.io/static/v1.svg?label=GitHub&message=omni-coveragereporter-python&color=informational)](https://github.com/JEsperancinhaOrg/omni-coveragereporter-python)

[![GitHub License](https://img.shields.io/badge/license-Apache%20License%202.0-blue.svg?style=flat)](https://www.apache.org/licenses/LICENSE-2.0)

[![GitHub release](https://img.shields.io/github/v/release/jesperancinhaorg/omni-coveragereporter-python)](https://github.com/jesperancinhaorg/omni-coveragereporter-python/releases)
[![PyPI](https://img.shields.io/pypi/v/omni-coveragereporter)](https://pypi.org/project/omni-coveragereporter/)

[![omni-coveragereporter-python](https://github.com/JEsperancinhaOrg/omni-coveragereporter-python/actions/workflows/python-package.yml/badge.svg)](https://github.com/JEsperancinhaOrg/omni-coveragereporter-python/actions/workflows/python-package.yml)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/f25fb0adabc74f129271fed966b6e8fa)](https://www.codacy.com/gh/JEsperancinhaOrg/omni-coveragereporter-python/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=JEsperancinhaOrg/omni-coveragereporter-python&amp;utm_campaign=Badge_Grade)

[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/f25fb0adabc74f129271fed966b6e8fa)](https://www.codacy.com/gh/JEsperancinhaOrg/omni-coveragereporter-python/dashboard?utm_source=github.com&utm_medium=referral&utm_content=JEsperancinhaOrg/omni-coveragereporter-python&utm_campaign=Badge_Coverage)
[![Coverage Status](https://coveralls.io/repos/github/JEsperancinhaOrg/omni-coveragereporter-python/badge.svg?branch=main)](https://coveralls.io/github/JEsperancinhaOrg/omni-coveragereporter-python?branch=main)
[![codecov](https://codecov.io/gh/JEsperancinhaOrg/omni-coveragereporter-python/branch/main/graph/badge.svg?token=NBlnQ2Qb1D)](https://codecov.io/gh/JEsperancinhaOrg/omni-coveragereporter-python)

[![GitHub language count](https://img.shields.io/github/languages/count/jesperancinhaorg/omni-coveragereporter-python.svg)](#)
[![GitHub top language](https://img.shields.io/github/languages/top/jesperancinhaorg/omni-coveragereporter-python.svg)](#)
[![GitHub top language](https://img.shields.io/github/languages/code-size/jesperancinhaorg/omni-coveragereporter-python.svg)](#)

## Intro

I created this plugin to support my exclusive Python projects. This is a spin-off project from the original one I've created to support my maven projects
on [![Generic badge](https://img.shields.io/static/v1.svg?label=GitHub&message=omni-coveragereporter-maven-plugin&color=informational)](https://github.com/JEsperancinhaOrg/omni-reporter-maven-plugin).

Current version is very limited by comparison and not much is configurable.

You can find a working example on the projects listed in the table below.

## Features

#### 1.  Reporting file supported

| Type             | Status | Notes                                                         | Available from Release | Example Project                                                                                                                                                                        |
|------------------|-------|---------------------------------------------------------------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Coverage Py JSON | ✅     | Coverage PY JSON file(s) must be generated in the root folder | 0.0.0                  | [![Generic badge](https://img.shields.io/static/v1.svg?label=GitHub&message=Med%20Dicom%20Service🏥&color=informational)](https://github.com/jesperancinha/med_dicom_service)          |
| Coverage GoLang  | ✅     | Coverage files created by Go                                  | 0.0.2                  | [![Generic badge](https://img.shields.io/static/v1.svg?label=GitHub&message=Multi%20Image%20Comparer%20🏞&color=informational)](https://github.com/jesperancinha/multi-image-comparer) |
| Clover           | ✅     | Clover files created by coverage tools                        | 0.0.3                  | [![Generic badge](https://img.shields.io/static/v1.svg?label=GitHub&message=Web%20Parser%20CSV&color=informational)](https://github.com/jesperancinha/web-parser-csv)                  |

#### 2.  Online API's supported

| Type       | Status | Notes | Environment Variables                                                                                                                                                                                     | Available from Release |
|------------|--------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| Coveralls  | ✅     |       | `COVERALLS_REPO_TOKEN` or `COVERALLS_TOKEN`                                                                                                                                                               | 0.0.0                  |
| Codacy     | ✅      |       | `CODACY_PROJECT_TOKEN`                                                                                                                                                                                    | 0.0.0                  |
| CodeCov    | ✅      |       | `CODECOV_TOKEN`                                                                                                                                                                                           | 0.0.0                  |

## Run Locally

```shell
python3 omni_coveragereporter_python.py
```

## Run Coverage

```shell
coverage run --source=omni-coveragereporter-python -m pytest
coverage run --source=omni-coveragereporter-python -m pytest  --capture=no 
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

pip3 install dist/omni_coveragereporter-0.0.3.tar.gz

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

## Test files

In all Omni projects, there are test files scattered all over the place. This is needed to see how the application behaves in different test scenarios. To keep things organized, this is the list of the files that are here specifically for test purposes:

-   [coverage.out](./coverage.out)
-   [coverage-pc.out](./coverage-pc.out)
-   [coverage-tc.out](./coverage-tc.out)
-   [pearson-correlation-coefficient](./pearson-correlation-coefficient)
-   [tanimoto-correlation-coefficient](./tanimoto-correlation-coefficient)
-   [points](./points)
-   [reports](./reports)
-   [clover.xml](./clover.xml)
-   [src](./src)

---

## References

-   [Codecov Report Upload](https://docs.codecov.com/reference/upload)
-   [Codacy Coverage Reporter](https://github.com/codacy/codacy-coverage-reporter)
-   [Jackson Module](https://medium.com/@foxjstephen/how-to-actually-parse-xml-in-java-kotlin-221a9309e6e8)
-   [XCode Environment Variable Reference](https://developer.apple.com/documentation/xcode/environment-variable-reference)
-   [Cross-CI reference](https://github.com/streamich/cross-ci)
-   [Coveralls API reference](https://docs.coveralls.io/api-reference)
-   [Git Hub Environment Variables](https://docs.github.com/en/actions/learn-github-actions/environment-variables)
-   [Git Lab Environment Variables](https://docs.gitlab.com/ee/ci/variables/predefined_variables.html)
-   [Check Run Reporter](https://github.com/marketplace/check-run-reporter)
-   [Codacy Maven Plugin](https://github.com/halkeye/codacy-maven-plugin)
-   [Coveralls Maven Plugin](https://github.com/trautonen/coveralls-maven-plugin)
-   [Example Java Maven for CodeCov](https://github.com/codecov/example-java-maven)
-   [CodeCov Maven Plugin](https://github.com/alexengrig/codecov-maven-plugin)

## About me 👨🏽‍💻🚀🏳️‍🌈

[![alt text](https://raw.githubusercontent.com/jesperancinha/project-signer/master/project-signer-templates/icons-20/JEOrgLogo-20.png "João Esperancinha Homepage")](http://joaofilipesabinoesperancinha.nl)
[![GitHub followers](https://img.shields.io/github/followers/jesperancinha.svg?label=Jesperancinha&style=social "GitHub")](https://github.com/jesperancinha)
[![Twitter Follow](https://img.shields.io/twitter/follow/joaofse?label=João%20Esperancinha&style=social "Twitter")](https://twitter.com/joaofse)
[![alt text](https://raw.githubusercontent.com/jesperancinha/project-signer/master/project-signer-templates/icons-20/mastodon-20.png "Mastodon")](https://masto.ai/@jesperancinha)
| [Sessionize](https://sessionize.com/joao-esperancinha/)
| [Spotify](https://open.spotify.com/user/jlnozkcomrxgsaip7yvffpqqm?si=b54b89eae8894960)
| [Medium](https://medium.com/@jofisaes)
| [Buy me a coffee](https://www.buymeacoffee.com/jesperancinha)
| [Credly Badges](https://www.credly.com/users/joao-esperancinha)
| [Google Apps](https://play.google.com/store/apps/developer?id=Joao+Filipe+Sabino+Esperancinha)
| [Sonatype Search Repos](https://search.maven.org/search?q=org.jesperancinha)
| [Docker Images](https://hub.docker.com/u/jesperancinha)
| [Stack Overflow Profile](https://stackoverflow.com/users/3702839/joao-esperancinha)
| [Reddit](https://www.reddit.com/user/jesperancinha/)
| [Dev.TO](https://dev.to/jofisaes)
| [Hackernoon](https://hackernoon.com/@jesperancinha)
| [Code Project](https://www.codeproject.com/Members/jesperancinha)
| [BitBucket](https://bitbucket.org/jesperancinha)
| [GitLab](https://gitlab.com/jesperancinha)
| [Coursera](https://www.coursera.org/user/da3ff90299fa9297e283ee8e65364ffb)
| [FreeCodeCamp](https://www.freecodecamp.org/jofisaes)
| [HackerRank](https://www.hackerrank.com/jofisaes)
| [LeetCode](https://leetcode.com/jofisaes)
| [Codebyte](https://coderbyte.com/profile/jesperancinha)
| [CodeWars](https://www.codewars.com/users/jesperancinha)
| [Code Pen](https://codepen.io/jesperancinha)
| [Hacker Earth](https://www.hackerearth.com/@jofisaes)
| [Khan Academy](https://www.khanacademy.org/profile/jofisaes)
| [Hacker News](https://news.ycombinator.com/user?id=jesperancinha)
| [InfoQ](https://www.infoq.com/profile/Joao-Esperancinha.2/)
| [LinkedIn](https://www.linkedin.com/in/joaoesperancinha/)
| [Xing](https://www.xing.com/profile/Joao_Esperancinha/cv)
| [Tumblr](https://jofisaes.tumblr.com/)
| [Pinterest](https://nl.pinterest.com/jesperancinha/)
| [Quora](https://nl.quora.com/profile/Jo%C3%A3o-Esperancinha)
| [VMware Spring Professional 2021](https://www.credly.com/badges/762fa7a4-9cf4-417d-bd29-7e072d74cdb7)
| [Oracle Certified Professional, Java SE 11 Programmer](https://www.credly.com/badges/87609d8e-27c5-45c9-9e42-60a5e9283280)
| [Oracle Certified Professional, JEE7 Developer](https://www.credly.com/badges/27a14e06-f591-4105-91ca-8c3215ef39a2)
| [IBM Cybersecurity Analyst Professional](https://www.credly.com/badges/ad1f4abe-3dfa-4a8c-b3c7-bae4669ad8ce)
| [Certified Advanced JavaScript Developer](https://cancanit.com/certified/1462/)
| [Certified Neo4j Professional](https://graphacademy.neo4j.com/certificates/c279afd7c3988bd727f8b3acb44b87f7504f940aac952495ff827dbfcac024fb.pdf)
| [Deep Learning](https://www.credly.com/badges/8d27e38c-869d-4815-8df3-13762c642d64)
| [![Generic badge](https://img.shields.io/static/v1.svg?label=GitHub&message=JEsperancinhaOrg&color=yellow "jesperancinha.org dependencies")](https://github.com/JEsperancinhaOrg)
[![Generic badge](https://img.shields.io/static/v1.svg?label=All%20Badges&message=Badges&color=red "All badges")](https://joaofilipesabinoesperancinha.nl/badges)
[![Generic badge](https://img.shields.io/static/v1.svg?label=Status&message=Project%20Status&color=red "Project statuses")](https://github.com/jesperancinha/project-signer/blob/master/project-signer-quality/Build.md)
