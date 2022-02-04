import os

import git
import requests

url = 'https://api.codacy.com'

repo = git.Repo(os.getcwd())
master = repo.head.reference
commit = master.commit.hexsha


def send_report(reports_pack):
    headers = {
        'Content-Type': 'application/json',
        'project-token': os.getenv('CODACY_PROJECT_TOKEN'),
    }
    if len(reports_pack.values()) == 1:
        effective_url = f'{url}/2.0/coverage/{commit}/{reports_pack.values[0].capitalized()}?partial=false'
        print(f"- Sending Codacy report to {effective_url}")
        r = requests.post(url=effective_url, headers=headers, data=reports_pack.values[0])
        return r.content.decode("utf-8")
    else:
        for lang in reports_pack.keys():
            effective_url = f'{url}/2.0/coverage/{commit}/{lang}?partial=true'
            print(f"- Sending Codacy report to {effective_url}")
            for report in reports_pack.values():
                print(report)
                r = requests.post(url=effective_url, headers=headers, data=report)
                print("- Codacy Report sent!")
                print(f"- {r.content.decode('utf-8')}")
            effective_final_url = f'{url}/2.0/commit/{commit}/coverageFinal'
            print(f"- Sending Final Codacy report to {effective_final_url}")
            final_response = requests.post(url=effective_final_url, headers=headers, json="")
            final_response.content.decode("utf-8")
    return None
