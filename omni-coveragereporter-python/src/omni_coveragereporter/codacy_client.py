import json
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
    reports_pack_keys = reports_pack.keys()
    first_key = list(reports_pack_keys)[0]
    if len(reports_pack_keys) == 1 and len(reports_pack[first_key]) == 1:
        effective_url = f'{url}/2.0/coverage/{commit}/{first_key}?partial=false'
        print(f"- Sending Codacy report to {effective_url}")
        r = requests.post(url=effective_url, headers=headers, data=json.dumps(reports_pack[first_key][0]))
        return r.content.decode("utf-8")
    else:
        for lang in reports_pack_keys:
            effective_url = f'{url}/2.0/coverage/{commit}/{lang}?partial=true'
            print(f"- Sending Codacy report to {effective_url}")
            for report in reports_pack[lang]:
                r = requests.post(url=effective_url, headers=headers, data=json.dumps(report))
                print("- Codacy Report sent!")
                print(f"- {r.content.decode('utf-8')}")
        effective_final_url = f'{url}/2.0/commit/{commit}/coverageFinal'
        print(f"- Sending Final Codacy report to {effective_final_url}")
        final_response = requests.post(url=effective_final_url, headers=headers, json="")
        final_response.content.decode("utf-8")
    return None
