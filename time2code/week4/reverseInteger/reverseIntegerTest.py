import pytest
from reverseInteger import reverseInteger

def testEmpty():
    assert reverseInteger("") == ""

def testNoCommaNum():
    assert reverseInteger("12345") == "54321"

def testCommaNum():
    assert reverseInteger("1,234") == "4,321"
    assert reverseInteger("1,234,567") == "7,654,321"

def testZeroTrailing():
    assert reverseInteger("3,200") == "23"

