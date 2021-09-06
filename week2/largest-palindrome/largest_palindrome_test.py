import pytest
from largest_palindrome import largestPalindrome

@pytest.mark.parametrize("input", [123,121])
def testInvalidInput(input):
    with pytest.raises(TypeError):
        largestPalindrome(input)

@pytest.mark.parametrize("input,expected", [("banana", "anana"),
                                                ("hh", "hh"),
                                                ("a", "a"),
                                                ("","")])
def testPalindrome(input, expected):
    assert largestPalindrome(input) == expected




 