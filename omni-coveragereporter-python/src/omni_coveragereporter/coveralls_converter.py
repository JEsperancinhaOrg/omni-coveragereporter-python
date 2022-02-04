import hashlib
import os

import git

import common
import coveragego_parser
import coveragepy_parser

repo = git.Repo(os.getcwd())
master = repo.head.reference
commit = master.commit
commitHex = commit.hexsha


def merge_coverage(existing_file, source_file):
    target = existing_file['coverage']
    source = source_file['coverage']
    for index in range(0, len(source)):
        target[index] = source[index] if target[index] is None else target[index] + source[index]
    return target


def create_coveralls_common(report):
    if report:
        coveralls_files = report['source_files']
        coveralls_report = report
    else:
        coveralls_report = {
            'repo_token': os.getenv('COVERALLS_REPO_TOKEN'),
            'service_name': 'local-ci'}
        head = {
            'id': commitHex,
            'author_name': commit.author.name,
            'author_email': commit.author.email,
            'committer_name': commit.committer.name,
            'committer_email': commit.committer.email,
            'message': commit.message
        }
        remotes = list(map(lambda remote: {'name': remote.name, 'url': remote.url}, repo.remotes))
        git_repo = {
            'head': head,
            'branch': repo.active_branch.name,
            'remotes': remotes
        }
        coveralls_report['git'] = git_repo
        coveralls_files = []
        coveralls_report['source_files'] = coveralls_files
    return coveralls_files, coveralls_report


def convert_coverage_py(data, report=None):
    coveralls_files, coveralls_report = create_coveralls_common(report)
    source_files = coveralls_report['source_files']
    for file_name in data['files']:
        if common.valid(file_name):
            file_object = data['files'][file_name]
            text_file = open(file_name, "r")
            file_content_bytes = text_file.read().encode('utf-8')
            total_lines = coveragepy_parser.total_lines(file_object) + 2
            line_coverage = [None] * total_lines
            executed_lines = file_object['executed_lines']
            for entry in executed_lines:
                line_coverage[entry - 1] = 1
            missing_lines = file_object['missing_lines']
            for entry in missing_lines:
                line_coverage[entry - 1] = 0
            source_file = {
                'name': file_name,
                'source_digest': hashlib.md5(file_content_bytes).hexdigest(),
                'coverage': line_coverage,
            }
            filter_result = list(filter(lambda file: file['name'] == file_name, coveralls_files))
            existing_file = filter_result[0] if len(filter_result) > 0 else None
            if existing_file is None:
                source_files.append(source_file)
            else:
                existing_file['coverage'] = merge_coverage(existing_file, source_file)

    return coveralls_report


def convert_coverage_go(data_text, report=None):
    coveralls_files, coveralls_report = create_coveralls_common(report)
    total_lines = 0
    total_coverage = 0
    all_lines = data_text.split("\n")
    for i in range(1, len(all_lines)):
        coverage_line = all_lines[i]
        if len(coverage_line) > coveragego_parser.MINIMAL_STATS_LENGTH:
            file_stats = coverage_line.split(":")
            absolute_file_name = file_stats[0]
            report_file_name = absolute_file_name.replace(os.getcwd(), '')
            if report_file_name.startswith("/"):
                report_file_name = report_file_name[1:]
            total_lines = coveragego_parser.total_lines(absolute_file_name)
            filter_result = list(filter(lambda file: file['name'] == report_file_name, coveralls_files))
            current_file_object = filter_result[0] if len(filter_result) > 0 else None
            if current_file_object is None:
                line_coverage = [None] * total_lines
                text_file = open(absolute_file_name, "r")
                file_content_bytes = text_file.read().encode('utf-8')
                current_file_object = {
                    'name': report_file_name,
                    'source_digest': hashlib.md5(file_content_bytes).hexdigest(),
                    "coverage": line_coverage
                }
                coveralls_files.append(current_file_object)

            coverage_lines = current_file_object['coverage']
            branch_line = file_stats[1].split(",")
            go_line_coverage = branch_line[1]
            line = go_line_coverage.split(".")[0]
            hits = go_line_coverage.split(" ")[2]
            back = int(go_line_coverage.split(" ")[1])
            coveragego_parser.merge(coverage_lines, int(line) - 1, int(hits))
            for i_back in range(1, back):
                coveragego_parser.merge(coverage_lines, int(line) - i_back - 1, int(hits))

    return coveralls_report
