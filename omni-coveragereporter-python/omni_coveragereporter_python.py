import json

import codecov_converter
import codecov_client

f = open('coverage.json')

data = json.load(f)

f.close()

codecov_report = codecov_converter.convert_coverage(data)

print(json.dumps(codecov_report))

codecov_report = codecov_converter.convert_coverage(data, codecov_report)

print(json.dumps(codecov_report))

report = codecov_client.send_report([json.dumps(codecov_report)])

print(report)
