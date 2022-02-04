#!/usr/bin/python
import glob
import json
import os

import codacy_client
import codacy_converter
import codecov_client
import codecov_converter
import coveralls_client
import coveralls_converter
from report_detector import is_coverage_go
from report_detector import is_coverage_py

banner = """
  ______   .___  ___. .__   __.  __     .______       _______ .______     ______   .______     .___________. _______ .______
 /  __  \  |   \/   | |  \ |  | |  |    |   _  \     |   ____||   _  \   /  __  \  |   _  \    |           ||   ____||   _  \ 
|  |  |  | |  \  /  | |   \|  | |  |    |  |_)  |    |  |__   |  |_)  | |  |  |  | |  |_)  |   `---|  |----`|  |__   |  |_)  |
|  |  |  | |  |\/|  | |  . `  | |  |    |      /     |   __|  |   ___/  |  |  |  | |      /        |  |     |   __|  |      /
|  `--'  | |  |  |  | |  |\   | |  |    |  |\  \----.|  |____ |  |      |  `--'  | |  |\  \----.   |  |     |  |____ |  |\  \----.
 \______/  |__|  |__| |__| \__| |__|    | _| `._____||_______|| _|       \______/  | _| `._____|   |__|     |_______|| _| `._____|

<Experimental Python Version>

by João Esperancinha
"""


def create_reports(all_report_texts):
    print(banner)
    codacy_reports = {}
    codecov_report = None
    coveralls_report = None
    for data_text in all_report_texts:
        codecov_token = os.getenv('CODECOV_TOKEN')
        if codecov_token is not None:
            print("Processing Codecov reports...")
            if is_coverage_py(data_text):
                codecov_report = codecov_converter.convert_coverage_py(json.loads(data_text), codecov_report)
            elif is_coverage_go(data_text):
                codecov_report = codecov_converter.convert_coverage_go(data_text, codecov_report)
        else:
            print("* CODECOV_TOKEN not configured.")

        coveralls_token = os.getenv('COVERALLS_REPO_TOKEN')
        if coveralls_token is not None:
            print("Processing Coveralls reports...")
            if is_coverage_py(data_text):
                coveralls_report = coveralls_converter.convert_coverage_py(json.loads(data_text), coveralls_report)
            elif is_coverage_go(data_text):
                coveralls_report = coveralls_converter.convert_coverage_go(data_text, coveralls_report)
        else:
            print("* COVERALLS_REPO_TOKEN not configured.")

        codacy_token = os.getenv('CODACY_PROJECT_TOKEN')
        if codacy_token is not None:
            print("Processing Codacy reports...")
            if is_coverage_py(data_text):
                py_report = codacy_converter.convert_coverage_py(json.loads(data_text))
                python_lang = codacy_converter.Language.PYTHON.capitalized()
                if python_lang not in codacy_reports:
                    codacy_reports[python_lang] = []
                codacy_reports[python_lang].append(py_report)
            elif is_coverage_go(data_text):
                go_report = codacy_converter.convert_coverage_go(data_text)
                go_lang = codacy_converter.Language.GO.capitalized()
                if go_lang not in codacy_reports:
                    codacy_reports[go_lang] = []
                if go_report is not None:
                    codacy_reports[go_lang].append(go_report)
        else:
            print("* CODACY_PROJECT_TOKEN not configured.")

    if codecov_report is not None:
        print(codecov_client.send_report([json.dumps(codecov_report)]))
        print("Codecov reporting complete!")

    if coveralls_report is not None:
        print(coveralls_client.send_report(json.dumps(coveralls_report)))
        print("Coveralls reporting complete!")

    if len(codacy_reports.values()) > 0:
        print(codacy_client.send_report(codacy_reports))
        print("Codacy reporting complete!")


def get_text_from_file(file_name):
    f = open(file_name)
    data = f.read()
    f.close()
    return data


if __name__ == '__main__':
    allDocs = []
    coveragePyDocs = [name for name in glob.glob("coverage*.json")]
    coverageGoDocs = [name for name in glob.glob("coverage*.out")]
    allDocs.extend(coveragePyDocs)
    allDocs.extend(coverageGoDocs)

    print(f"- Found potential report files {allDocs}")

    allDocs = map(lambda file: get_text_from_file(file), allDocs)

    create_reports(allDocs)
