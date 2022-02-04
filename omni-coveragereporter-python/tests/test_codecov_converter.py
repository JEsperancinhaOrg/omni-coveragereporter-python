import json
import os
import sys

sys.path.insert(0, os.path.abspath('../src/omni_coveragereporter'))
sys.path.insert(0, os.path.abspath('src/omni_coveragereporter'))
sys.path.insert(0, os.path.abspath('omni-coveragereporter-python/src/omni_coveragereporter'))

import codecov_converter
from omni_coveragereporter_python import get_text_from_file


def test_convert_coverage_go():
    text_from_file = get_text_from_file("coverage.out").replace("${test}", f'{os.getcwd()}/points')
    coverage_go_report = codecov_converter.convert_coverage_go(text_from_file)

    dumps = json.loads(
        "{\"coverage\": {\"/points/image-utils.go\": {\"1\": null, \"2\": null, \"3\": null, \"4\": null, \"5\": null, " \
        "\"6\": null, \"7\": null, \"8\": null, \"9\": null, \"10\": null, \"11\": null, \"12\": null, \"13\": null, " \
        "\"14\": null, \"15\": null, \"16\": \"1\", \"17\": 1, \"18\": null, \"19\": 1, \"20\": null, \"21\": null, \"22\": 1, " \
        "\"23\": null, \"24\": null, \"25\": 1, \"26\": null, \"27\": null, \"28\": 1, \"29\": null, \"30\": 1, \"31\": null}}}")

    assert coverage_go_report == dumps
