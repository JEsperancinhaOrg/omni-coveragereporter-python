import os

import git
import requests

url = 'https://api.codacy.com'

repo = git.Repo(os.getcwd())
master = repo.head.reference
commit = master.commit.hexsha


# val codacyReportUrl = "$url/2.0/coverage/$commitId/${language.lang}?partial=${partial}"
# logger.info("Sending ${language.name.lowercase()} report to codacy at $codacyReportUrl")
# val jsonReport = writeCamelCaseJsonValueAsString(report)
# logger.debug(jsonReport.redact(token).redact(apiToken?.codacyApiToken))
# val content: HttpContent = ByteArrayContent(ContentType.APPLICATION_JSON.mimeType, jsonReport.toByteArray())
# val httpRequest = httpRequestFactory.buildPostRequest(GenericUrl(codacyReportUrl), content)
# httpRequest.headers.contentType = ContentType.APPLICATION_JSON.mimeType
# httpRequest.headers["project-token"] = token
# httpRequest.isLoggingEnabled = false
# val httpResponse = httpRequest?.execute()
# val readAllBytes = httpResponse?.content?.readAllBytes() ?: byteArrayOf()
# return readJsonValue(readAllBytes)


# val codacyReportUrl = "$url/2.0/commit/$commitId/coverageFinal"
# logger.info("Sending Final ${language.name.lowercase()} report to codacy at $codacyReportUrl")
# val httpRequest = httpRequestFactory.buildPostRequest(
#     GenericUrl(codacyReportUrl),
#     ByteArrayContent(ContentType.APPLICATION_JSON.mimeType, "".toByteArray())
# )
# httpRequest.headers.contentType = ContentType.APPLICATION_JSON.mimeType
# httpRequest.headers["project-token"] = token
# httpRequest.isLoggingEnabled = false
# val httpResponse = httpRequest?.execute()
# val readAllBytes = httpResponse?.content?.readAllBytes() ?: byteArrayOf()
# return readJsonValue(readAllBytes)

def send_report(reports, language):
    headers = {
        'Content-Type': 'application/json',
        'project-token': os.getenv('CODACY_PROJECT_TOKEN'),
    }
    if len(reports) == 1:
        effective_url = f'{url}/2.0/coverage/{commit}/{language.capitalized()}?partial=false'
        r = requests.post(url=effective_url, headers=headers, json=reports[0])
        return r.content.decode("utf-8")
    else:
        effective_url = f'{url}/2.0/coverage/{commit}/{language}?partial=true'
        for report in reports:
            r = requests.post(url=effective_url, headers=headers, json=report)
            print("- Codacy Report sent!")
            print(f"- {r.content.decode('utf-8')}")
        effective_final_url = f'{url}/2.0/commit/{commit}/coverageFinal'
        final_response = requests.post(url=effective_final_url, headers=headers, json="")
        final_response.content.decode("utf-8")
    return None
