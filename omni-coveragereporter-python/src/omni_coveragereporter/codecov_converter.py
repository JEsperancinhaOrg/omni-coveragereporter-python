import os

import common
import coveragego_parser
import coveragepy_parser


def convert_coverage_py(data, report=None):
    if report:
        codecov_files = report['coverage']
        codecov_report = report
    else:
        codecov_files = {}
        codecov_report = {"coverage": codecov_files}
    for file_name in data['files']:
        if common.valid(file_name):
            file_object = data['files'][file_name]
            total_lines = coveragepy_parser.total_lines(file_object)
            codecov_file = codecov_files[file_name] if file_name in codecov_files else None
            if codecov_file is None:
                codecov_file = {}
                codecov_files[file_name] = codecov_file
            for i in range(1, total_lines):
                if str(i) in codecov_file:
                    curr = 0 if codecov_file[str(i)] is None else codecov_file[str(i)]
                    offset = 1 if i in file_object['executed_lines'] else 0
                    codecov_file[str(i)] = curr + offset
                else:
                    codecov_file[str(i)] = 1 if i in file_object['executed_lines'] else None
                if codecov_file[str(i)] is None:
                    codecov_file[str(i)] = 0 if i in file_object['missing_lines'] else None
    return codecov_report


def convert_coverage_go(data_text, report=None):
    if report:
        codecov_files = report['coverage']
        codecov_report = report
    else:
        codecov_files = {}
        codecov_report = {"coverage": codecov_files}

    all_lines = data_text.split("\n")

    for i in range(1, len(all_lines)):
        coverage_line = all_lines[i]
        if len(coverage_line) > coveragego_parser.MINIMAL_STATS_LENGTH:
            file_stats = coverage_line.split(":")
            absolute_file_name = file_stats[0]
            report_file_name = absolute_file_name.replace(os.getcwd(), '')
            codecov_file = codecov_files[report_file_name] if report_file_name in codecov_files else None
            if codecov_file is None:
                codecov_file = {}
                codecov_files[report_file_name] = codecov_file
                total_lines = coveragego_parser.total_lines(absolute_file_name)
                for line in range(1, total_lines + 1):
                    codecov_file[str(line)] = None

            branch_line = file_stats[1].split(",")
            line_coverage = branch_line[1]
            line = line_coverage.split(".")[0]
            hits = line_coverage.split(" ")[2]
            back = int(line_coverage.split(" ")[1])
            codecov_file[line] = int(hits)
            for i_back in range(1, back):
                codecov_file[str(int(line) - i_back)] = int(hits)

    return codecov_report
