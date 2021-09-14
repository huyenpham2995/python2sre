import pytest
from fibonacci import find_nth_fibonacci

def testNegativeN():
    assert find_nth_fibonacci(-1) == None

def testZero():
    assert find_nth_fibonacci(0) == None

def testNNotInteger():
    assert find_nth_fibonacci(2.5) == None

def testFirstFibonnaci():
    assert find_nth_fibonacci(1) == 0

def testSecondFibonnaci():
    assert find_nth_fibonacci(2) == 1

def testValidN():
    assert find_nth_fibonacci(6) == 5