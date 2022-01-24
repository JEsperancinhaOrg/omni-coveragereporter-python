import hashlib
import os

import git

import coveragepy_parser

repo = git.Repo(os.getcwd())
master = repo.head.reference
commit = master.commit
commitHex = commit.hexsha


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
    for fileName in data['files']:
        file_object = data['files'][fileName]
        text_file = open(fileName, "r")
        file_content_bytes = text_file.read().encode('utf-8')
        total_lines = coveragepy_parser.total_lines(file_object)
        line_coverage = [None] * total_lines
        executed_lines = file_object['executed_lines']
        for entry in executed_lines:
            print(total_lines)
            print(entry)
            line_coverage[entry - 1] = 1 if entry in executed_lines else 0
        source_file = {
            'name': fileName,
            'sourceDigest': hashlib.md5(file_content_bytes).hexdigest(),
            'coverage': line_coverage,
        }
        source_files.append(source_file)

    return coveralls_report
