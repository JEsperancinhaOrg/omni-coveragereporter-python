import json

f = open('reports/coverage.json')

data = json.load(f)

f.close()

print(data)
