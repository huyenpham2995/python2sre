import pytest
from fibonacci import findNthFibonacci

def testNegativeN():
    assert findNthFibonacci(-1) == None

def testZero():
    assert findNthFibonacci(0) == None

def testNNotInteger():
    assert findNthFibonacci(2.5) == None

def testFirstFibonnaci():
    assert findNthFibonacci(1) == 0

def testSecondFibonnaci():
    assert findNthFibonacci(2) == 1

def testValidN():
    assert findNthFibonacci(6) == 5