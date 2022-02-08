import os
import sys

from omni_coveragereporter_python import get_text_from_file
from report_detector import is_coverage_go
from report_detector import is_coverage_py
from report_detector import is_clover

sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('../src/omni_coveragereporter'))
sys.path.insert(0, os.path.abspath('omni-coveragereporter-python/src/omni_coveragereporter'))
sys.path.insert(0, os.path.abspath('src/omni_coveragereporter'))
sys.path.insert(0, os.path.abspath('../omni-coveragereporter-python/src/omni_coveragereporter'))


def test_is_coverage_py():
    text_from_file = get_text_from_file("reports/coverage.json")
    assert is_coverage_py(text_from_file) is True


def test_is_not_coverage_py():
    text_from_file = get_text_from_file("coverage.out")
    assert is_coverage_py(text_from_file) is False


def test_is_coverage_go():
    text_from_file = get_text_from_file("coverage.out")
    assert is_coverage_go(text_from_file) is True


def test_is_not_coverage_go():
    text_from_file = get_text_from_file("reports/coverage.json")
    assert is_coverage_go(text_from_file) is False


def test_is_clover():
    text_from_file = get_text_from_file("reports/clover.xml")
    assert is_clover(text_from_file) is True
