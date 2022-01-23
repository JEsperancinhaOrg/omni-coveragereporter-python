import json

import codecov_converter
import codecov_client

import coveralls_converter

f = open('coverage.json')
data = json.load(f)
f.close()

# codecov_report = codecov_converter.convert_coverage(data)
# print(json.dumps(codecov_report))
# codecov_report = codecov_converter.convert_coverage(data, codecov_report)
# print(json.dumps(codecov_report))
# report = codecov_client.send_report([json.dumps(codecov_report)])
# print(report)

coveralls_report = coveralls_converter.convert_coverage(data)
print(json.dumps(coveralls_report))
