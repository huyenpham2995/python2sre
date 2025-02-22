import pytest
from pangrams import is_pangrams

a = [1, 2, 3]
b = [2, 4, 6]

def testEmpty():
    assert is_pangrams("") == "not pangram"

def testIsPangram():
    assert is_pangrams("We promptly judged antique ivory buckles for the next prize") == "pangram"
    
def testNotPangram():
    assert is_pangrams("We promptly judged antique ivory buckles for the prize") == "not pangram"

def testSpecialChar():
    assert is_pangrams("We promptly judged antique ivory buckles for the prize $%") == "not pangram"