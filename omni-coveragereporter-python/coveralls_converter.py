import hashlib
import os

import git

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


def convert_coverage(data, report=None):
    if report:
        coveralls_files = report['sourceFiles']
        coveralls_report = report
    else:
        coveralls_files = {}
        coveralls_report = {
            'repoToken': os.getenv('COVERALLS_REPO_TOKEN'),
            'serviceName': 'local-ci'}
        head = {
            'id': commitHex,
            'authorName': commit.author.name,
            'authorEmail': commit.author.email,
            'committerName': commit.committer.name,
            'committerEmail': commit.committer.email,
            'message': commit.message
        }
        remotes = list(map(lambda remote: {'name': remote.name, 'url': remote.url}, repo.remotes))
        print(remotes)
        git_repo = {
            'head': head,
            'branch': repo.active_branch.name,
            'remotes': remotes
        }
        coveralls_report['git'] = git_repo
        coveralls_report['sourceFiles'] = []
    source_files = coveralls_report['sourceFiles']
    for file_name in data['files']:
        file_object = data['files'][file_name]
        text_file = open(file_name, "r")
        file_content_bytes = text_file.read().encode('utf-8')
        total_lines = coveragepy_parser.total_lines(file_object)
        line_coverage = [None] * total_lines
        executed_lines = file_object['executed_lines']
        for entry in executed_lines:
            line_coverage[entry - 1] = 1 if entry in executed_lines else 0
        source_file = {
            'name': file_name,
            'sourceDigest': hashlib.md5(file_content_bytes).hexdigest(),
            'coverage': line_coverage,
        }
        filter_result = list(filter(lambda file: file['name'] == file_name, coveralls_files))
        existing_file = filter_result[0] if len(filter_result) > 0 else None
        if existing_file is None:
            source_files.append(source_file)
        else:
            existing_file['coverage'] = merge_coverage(existing_file, source_file)

    return coveralls_report