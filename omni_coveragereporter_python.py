import json

import codecov_converter

f = open('reports/coverage.json')

data = json.load(f)

f.close()

codecov_report = codecov_converter.convert_coverage(data)

print(json.dumps(codecov_report))
