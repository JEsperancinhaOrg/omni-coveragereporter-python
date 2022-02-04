import json
import os
import sys

sys.path.insert(0, os.path.abspath('../src/omni_coveragereporter'))
sys.path.insert(0, os.path.abspath('src/omni_coveragereporter'))
sys.path.insert(0, os.path.abspath('omni-coveragereporter-python/src/omni_coveragereporter'))

import codacy_converter
from omni_coveragereporter_python import get_text_from_file


def test_capitalized():
    assert codacy_converter.Language.JAVA.capitalized() == 'Java'
    assert codacy_converter.Language.KOTLIN.capitalized() == 'Kotlin'
    assert codacy_converter.Language.SCALA.capitalized() == 'Scala'
    assert codacy_converter.Language.PYTHON.capitalized() == 'Python'
    assert codacy_converter.Language.JAVA_SCRIPT.capitalized() == 'JavaScript'


def test_convert_coverage_go():
    text_from_file = get_text_from_file("coverage.out").replace("${test}", f'{os.getcwd()}/points')
    coverage_go_report = codacy_converter.convert_coverage_go(text_from_file)
    assert len(json.dumps(coverage_go_report)) > 10
