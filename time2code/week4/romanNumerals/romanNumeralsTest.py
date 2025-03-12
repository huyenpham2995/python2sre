import pytest
from romanNumerals import romanNumerals

def testSimple():
    assert romanNumerals("III") == 3
    assert romanNumerals("X") == 10
    assert romanNumerals("XVII") == 17
    assert romanNumerals("CXXXVII") == 137

def testNotSimple():
    assert romanNumerals("IX") == 9
    assert romanNumerals("IV") == 4
    assert romanNumerals("XIX") == 19

def testLowerCase():
    assert romanNumerals("lv") == 55
    assert romanNumerals("cl") == 150

def testInvalid():
    assert romanNumerals("lz") == None





