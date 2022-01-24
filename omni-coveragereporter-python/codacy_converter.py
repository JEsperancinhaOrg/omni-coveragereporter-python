from enum import Enum

import coveragepy_parser


class Language(Enum):
    JAVA = 1
    KOTLIN = 2
    SCALA = 3
    PYTHON = 4
    JAVA_SCRIPT = 5

    def capitalized(self):
        name = self.name
        return "".join(list(map(lambda t: t.capitalize(), name.split("_"))))


def convert_coverage(data):
    data_files = data['files']
    total_covered = sum(map(lambda file_name: len(data_files[file_name]['executed_lines']), data_files))
    total_lines = sum(map(lambda file_name: len(data_files[file_name]['executed_lines']) + len(
        data_files[file_name]['missing_lines']), data_files))
    total_percent = total_covered * 100 / total_lines
    codacy_report = {}
    codacy_report['total'] = total_percent
    codacy_file_reports = []
    codacy_report['fileReports'] = codacy_file_reports

    for file_name in data_files:
        file_object = data_files[file_name]
        file_covered = len(file_object['executed_lines'])
        file_lines = len(file_object['executed_lines']) + len(file_object['missing_lines'])
        codacy_file_report = {}
        codacy_file_report['filename'] = file_name
        codacy_file_report['total'] = file_covered * 100 / file_lines
        line_coverage = {}
        for index in file_object['executed_lines']:
            line_coverage[str(index)] = 1
        for index in file_object['missing_lines']:
            line_coverage[str(index)] = 0
        codacy_file_reports.append(codacy_file_report)
        codacy_file_report['coverage'] = line_coverage
    return codacy_report
