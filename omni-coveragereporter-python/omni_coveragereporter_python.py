import json

import codacy_client
import codacy_converter
import codecov_client
import codecov_converter
import coveralls_client
import coveralls_converter

f = open('coverage.json')
data = json.load(f)
f.close()

codecov_report = codecov_converter.convert_coverage(data)
print(json.dumps(codecov_report))
report = codecov_client.send_report([json.dumps(codecov_report)])
print(report)

coveralls_report = coveralls_converter.convert_coverage(data)
print(json.dumps(coveralls_report))
report = coveralls_client.send_report(json.dumps(coveralls_report))
print(report)

codacy_report = codacy_converter.convert_coverage(data)
print(json.dumps(codacy_report))
report = codacy_client.send_report([json.dumps(codacy_report)], codacy_converter.Language.PYTHON)
print(report)
