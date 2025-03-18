import pytest
from reverse_words_in_string import reverse_words

def testEmpty():
    assert reverse_words("") == ""

def testNormalString():
    assert reverse_words("the sky is blue") == "blue is sky the"
    
def testStringWithLeadingTrailingSpaces():
    assert reverse_words("  hello world  ") == "world hello"

def testStringWithMultipleSpaces():
    assert reverse_words("  a good   example") == "example good a"