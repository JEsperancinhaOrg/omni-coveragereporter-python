import json
import os
import sys

sys.path.insert(0, os.path.abspath('../src/omni_coveragereporter'))
sys.path.insert(0, os.path.abspath('src/omni_coveragereporter'))
sys.path.insert(0, os.path.abspath('omni-coveragereporter-python/src/omni_coveragereporter'))
import xml.etree.ElementTree as ET
import codecov_converter
from omni_coveragereporter_python import get_text_from_file


def test_convert_coverage_go():
    text_from_file = get_text_from_file("coverage.out").replace("${test}", f'{os.getcwd()}/points')
    coverage_go_report = codecov_converter.convert_coverage_go(text_from_file)
    assert len(json.dumps(coverage_go_report)) > 10


def test_convert_clover():
    text_from_file = get_text_from_file("clover.xml").replace("${test}", f'{os.getcwd()}/src')
    coverage_clover_report = codecov_converter.convert_clover(ET.fromstring(text_from_file))
    assert len(json.dumps(coverage_clover_report)) > 10
