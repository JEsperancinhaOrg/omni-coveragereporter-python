import os

import git
import requests

repo = git.Repo(os.getcwd())
master = repo.head.reference
commit = master.commit.hexsha

url = 'https://codecov.io/upload/v4'

separator = "\n<<<<<< EOF\n"


def send_report(codecov_reports):
    print(commit)
    params = {
        'commit': commit,
        'token': os.getenv('CODECOV_TOKEN'),
        'branch': master
    }
    headers = {
        'Content-Type': 'text/plain'
    }
    r = requests.post(url, params=params, headers=headers, json="")
    decode = r.content.decode("utf-8").split(sep='\n')
    view = decode[0],
    upload_to_s3_url = decode[1]

    print(decode)
    codecov_report = separator.join(codecov_reports) + separator

    print(codecov_report)
    r = requests.post(upload_to_s3_url, headers=headers, json=codecov_report)
    return r.content.decode("utf-8")
