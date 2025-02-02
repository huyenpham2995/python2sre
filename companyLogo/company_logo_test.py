import pytest
from company_logo import company_logo


def test1():
    assert company_logo("aabbbccde") == [("b",3),("a",2),("c",2)]

def testAnd():
    assert company_logo("google") == [("g",2),("o",2),("e",1)]
    
def testEmpty():
    assert company_logo("") == []