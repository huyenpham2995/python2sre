import pytest
from reverse_vowels import reverse_vowels

def testEmptyString():
    assert reverse_vowels("") == ""

def test():
    assert reverse_vowels("IceCreAm") == "AceCreIm"
    assert reverse_vowels("leotcede") == "leotcede"