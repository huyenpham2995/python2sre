import pytest
from numeronym import verify_numeronym

def testEmptyWord():
    assert verify_numeronym("a2y", "") == False

def testZero():
    assert verify_numeronym("a0b", "ab") == True
    assert verify_numeronym("a0b", "acb") == False

def testLongString():
    assert verify_numeronym("i18n", "internationalization") == True
    assert verify_numeronym("g2o", "gato") == True
    assert verify_numeronym("y3o", "yoyoyo") == False
    