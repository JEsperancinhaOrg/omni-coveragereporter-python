import os
import tempfile

temporaryFolder = tempfile.gettempdir()

url = 'https://coveralls.io/api/v1/jobs'
coveralls_file = 'coveralls.json'

coveralls_tmp_file = os.path.join(temporaryFolder, coveralls_file)


def send_report(report):
    file_save = open(coveralls_tmp_file, "w")
    file_save.write(report)
    file_save.close()
    print(f"- Saved file in {file_save.name}")
    return None
