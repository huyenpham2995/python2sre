import pytest
from numeronym import verifyNumeronym

def testEmptyWord():
    assert verifyNumeronym("a2y", "") == False

def testZero():
    assert verifyNumeronym("a0b", "ab") == True
    assert verifyNumeronym("a0b", "acb") == False

def testLongString():
    assert verifyNumeronym("i18n", "internationalization") == True
    assert verifyNumeronym("g2o", "gato") == True
    assert verifyNumeronym("y3o", "yoyoyo") == False
    