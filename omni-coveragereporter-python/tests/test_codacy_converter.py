import os
import sys

sys.path.insert(0, os.path.abspath('../src/omni_coveragereporter'))
sys.path.insert(0, os.path.abspath('src/omni_coveragereporter'))
sys.path.insert(0, os.path.abspath('omni-coveragereporter-python/src/omni_coveragereporter'))

import codacy_converter


def test_capitalized():
    assert codacy_converter.Language.JAVA.capitalized() == 'Java'
    assert codacy_converter.Language.KOTLIN.capitalized() == 'Kotlin'
    assert codacy_converter.Language.SCALA.capitalized() == 'Scala'
    assert codacy_converter.Language.PYTHON.capitalized() == 'Python'
    assert codacy_converter.Language.JAVA_SCRIPT.capitalized() == 'JavaScript'
