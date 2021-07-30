import pytest
from largest_palindrome import largestPalindrome

def testEmptyString():
    assert largestPalindrome("") == ""

def testOneLetter():
    assert largestPalindrome("a") == "a"

def testOddString():
    assert largestPalindrome("banana") == "anana"

def testEvenString():
    assert largestPalindrome("hh") == "hh"

 