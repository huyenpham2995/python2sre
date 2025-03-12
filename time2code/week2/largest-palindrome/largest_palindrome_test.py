import pytest
from largest_palindrome import largest_palindrome

@pytest.mark.parametrize("input", [123,121])
def test_invalid_input(input):
    with pytest.raises(TypeError):
        largest_palindrome(input)

@pytest.mark.parametrize("input,expected", [("banana", "anana"),
                                                ("hh", "hh"),
                                                ("a", "a"),
                                                ("","")])
def test_palindrome(input, expected):
    assert largest_palindrome(input) == expected




 