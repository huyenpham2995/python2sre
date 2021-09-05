import pytest
from largest_palindrome import largestPalindrome

def testEmptyString():
    assert largestPalindrome("") == ""

def testOneLetter():
    assert largestPalindrome("a") == "a"

@pytest.mark.parametrize("testInput,expected", [("banana", "anana"), ("hh", "hh")])
def testPalindrome(testInput, expected):
    assert largestPalindrome(testInput) == expected



 