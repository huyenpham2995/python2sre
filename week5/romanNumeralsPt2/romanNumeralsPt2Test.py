import pytest
from romanNumeralsPt2 import romanNumeralsPt2

def testNormalCases():
    assert romanNumeralsPt2("XVI") == 16
    assert romanNumeralsPt2("XIV") == 14

def testWeirdCases():
    assert romanNumeralsPt2("IC") == 99
    assert romanNumeralsPt2("XVIC") == 84
    assert romanNumeralsPt2("IVX") == 6