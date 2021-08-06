import pytest
from numeronymPlus import verifyNumeronymPlus

def testEmpty():
    assert verifyNumeronymPlus("", "") == True
    assert verifyNumeronymPlus("a2y", "") == False
    assert verifyNumeronymPlus("", "aaa") == False

def testInvalidNumeronym():
    assert verifyNumeronymPlus("2t", "aat") == False
    assert verifyNumeronymPlus("b1", "be") == False