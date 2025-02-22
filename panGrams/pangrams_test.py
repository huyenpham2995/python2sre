import pytest
from pangrams import is_pangrams

def testEmpty():
    assert is_pangrams("") == "not pangram"

def testIsPangram():
    assert is_pangrams("We promptly judged antique ivory buckles for the next prize") == "pangram"
    
def testNotPangram():
    assert is_pangrams("We promptly judged antique ivory buckles for the prize") == "not pangram"

def testSpecialChar():
    assert is_pangrams("We promptly judged antique ivory buckles for the prize $%") == "not pangram"