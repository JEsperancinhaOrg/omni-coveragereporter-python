import json

import codacy_client
import codacy_converter
import codecov_client
import codecov_converter
import coveralls_client
import coveralls_converter

banner = """
  ______   .___  ___. .__   __.  __     .______       _______ .______     ______   .______     .___________. _______ .______
 /  __  \  |   \/   | |  \ |  | |  |    |   _  \     |   ____||   _  \   /  __  \  |   _  \    |           ||   ____||   _  \ 
|  |  |  | |  \  /  | |   \|  | |  |    |  |_)  |    |  |__   |  |_)  | |  |  |  | |  |_)  |   `---|  |----`|  |__   |  |_)  |
|  |  |  | |  |\/|  | |  . `  | |  |    |      /     |   __|  |   ___/  |  |  |  | |      /        |  |     |   __|  |      /
|  `--'  | |  |  |  | |  |\   | |  |    |  |\  \----.|  |____ |  |      |  `--'  | |  |\  \----.   |  |     |  |____ |  |\  \----.
 \______/  |__|  |__| |__| \__| |__|    | _| `._____||_______|| _|       \______/  | _| `._____|   |__|     |_______|| _| `._____|

<Experimental Python Version>

by João Esperancinha
"""

f = open('coverage.json')
data = json.load(f)
f.close()

print(banner)
print("Processing Codecov reports...")
codecov_report = codecov_converter.convert_coverage(data)
codecov_client.send_report([json.dumps(codecov_report)])
print("Codecov reporting complete!")

print("Processing Coveralls reports...")
coveralls_report = coveralls_converter.convert_coverage(data)
coveralls_client.send_report(json.dumps(coveralls_report))
print("Coveralls reporting complete!")

print("Processing Codacy reports...")
codacy_report = codacy_converter.convert_coverage(data)
codacy_client.send_report([json.dumps(codacy_report)], codacy_converter.Language.PYTHON)
print("Codacy reporting complete!")
