import pytest
from numeronymPlus import verifyNumeronymPlus

def testEmpty():
    assert verifyNumeronymPlus("", "") == True
    assert verifyNumeronymPlus("a2y", "") == False
    assert verifyNumeronymPlus("", "aaa") == False

def testSimpleNumerynom():
    assert verifyNumeronymPlus("i18n", "internationalization") == True
    assert verifyNumeronymPlus("g2o", "gato") == True
    assert verifyNumeronymPlus("y3o", "yoyoyo") == False

def testDifferentCharacter():
    assert verifyNumeronymPlus("ab1c", "bbbc") == False

def testDifferentLength():
    assert verifyNumeronymPlus("ab1c", "abc") == False
    assert verifyNumeronymPlus("ab1c", "abcdefgh") == False

def testNumberWithMoreThanOneDigit():
    assert verifyNumeronymPlus("ab10c", "abaaaaaaaaaac") == True
    assert verifyNumeronymPlus("ab03c", "abaaac") == False

def testNumberInDifferentPlaces():
    assert verifyNumeronymPlus("f1l1ne", "feline") == False

def testMoreThanOneLetter():
    assert verifyNumeronymPlus("ab1c", "abcc") == True

def testInvalidNumeronym():
    assert verifyNumeronymPlus("2t", "aat") == False
    assert verifyNumeronymPlus("b1", "be") == False