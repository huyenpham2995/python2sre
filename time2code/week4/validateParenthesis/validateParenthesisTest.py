import pytest
from validateParenthesis import validateParenthesis

def testEmpty():
    assert validateParenthesis("") == True

def testValid():
    assert validateParenthesis("()") == True

def testInvalid():
    assert validateParenthesis("())") == False
    assert validateParenthesis("()())))") == False


def testWithString():
    assert validateParenthesis("ab(bc(c)dc)") == True
    assert validateParenthesis("(asf(as(f)") == False



