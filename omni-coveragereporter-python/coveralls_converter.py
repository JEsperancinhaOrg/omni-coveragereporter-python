import os

import git

repo = git.Repo(os.getcwd())
master = repo.head.reference
commit = master.commit
commitHex = commit.hexsha


def convert_coverage(data):
    coverallls_report = {}
    coverallls_report['repoToken'] = os.getenv('COVERALLS_REPO_TOKEN')
    coverallls_report['serviceName'] = 'local-ci'
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
    source_files = {}
    coverallls_report['sourceFiles'] = source_files
    coverallls_report['git'] = git_repo
    return coverallls_report
