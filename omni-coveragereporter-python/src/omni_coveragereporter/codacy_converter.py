import os
from enum import Enum

import common
import coveragego_parser


class Language(Enum):
    JAVA = 1
    KOTLIN = 2
    SCALA = 3
    PYTHON = 4
    JAVA_SCRIPT = 5
    GO = 6

    def capitalized(self):
        name = self.name
        return "".join(list(map(lambda t: t.capitalize(), name.split("_"))))

    def ext(self):
        if self is Language.JAVA:
            return "java"
        if self is Language.KOTLIN:
            return "kt"
        if self is Language.SCALA:
            return "scala"
        if self is Language.PYTHON:
            return "py"
        if self is Language.JAVA_SCRIPT:
            return "js"
        if self is Language.GO:
            return "go"


def convert_coverage_py(data):
    data_files = data['files']
    total_covered = sum(map(lambda fn: len(data_files[fn]['executed_lines']), data_files))
    total_lines = sum(map(lambda fn: len(data_files[fn]['executed_lines']) + len(
        data_files[fn]['missing_lines']), data_files))
    total_percent = total_covered * 100 / total_lines
    codacy_report = {'total': int(total_percent)}
    codacy_file_reports = []
    codacy_report['fileReports'] = codacy_file_reports

    for file_name in data_files:
        if common.valid(file_name):
            file_object = data_files[file_name]
            file_covered = len(file_object['executed_lines'])
            file_lines = len(file_object['executed_lines']) + len(file_object['missing_lines'])
            codacy_file_report = {'filename': file_name, 'total': int(file_covered * 100 / file_lines)}
            line_coverage = {}
            for index in file_object['executed_lines']:
                line_coverage[str(index)] = 1
            for index in file_object['missing_lines']:
                line_coverage[str(index)] = 0
            codacy_file_reports.append(codacy_file_report)
            codacy_file_report['coverage'] = line_coverage
    return codacy_report


def convert_coverage_go(data_text):
    file_reports = []
    codacy_report = {
        'total': 0,
        'fileReports': file_reports
    }
    all_lines = data_text.split("\n")
    total_lines = 0
    total_coverage = 0

    for i in range(1, len(all_lines)):
        coverage_line = all_lines[i]
        if len(coverage_line) > coveragego_parser.MINIMAL_STATS_LENGTH:
            file_stats = coverage_line.split(":")
            absolute_file_name = file_stats[0]
            report_file_name = absolute_file_name.replace(os.getcwd(), '')
            if report_file_name.startswith("/"):
                report_file_name = report_file_name[1:]
            file_lines = coveragego_parser.total_lines(absolute_file_name)
            total_lines += file_lines
            filter_result = list(filter(lambda file: file['filename'] == report_file_name, file_reports))
            current_file_object = filter_result[0] if len(filter_result) > 0 else None
            if current_file_object is None:
                line_coverage = {}
                for line in range(1, file_lines + 1):
                    line_coverage[str(line)] = 0
                current_file_object = {
                    'filename': report_file_name,
                    'total': 0,
                    'coverage': line_coverage
                }
                file_reports.append(current_file_object)

            coverage_lines = current_file_object['coverage']
            branch_line = file_stats[1].split(",")
            line_coverage = branch_line[1]
            line = line_coverage.split(".")[0]
            hits = line_coverage.split(" ")[2]
            back = int(line_coverage.split(" ")[1])
            coverage_lines[line] = int(hits)
            total_coverage += 1 if int(hits) > 0 else 0
            for i_back in range(1, back):
                total_coverage += 1 if int(hits) > 0 else 0
                coverage_lines[str(int(line) - i_back)] = int(hits)
    codacy_report['total'] = int((total_coverage * 100) / total_lines)
    for source in file_reports:
        coverage_per_file = source["coverage"]
        source["total"] = int(
            (len(list(filter(lambda x: x > 0, coverage_per_file.values()))) * 100) / len(coverage_per_file))
    return codacy_report
