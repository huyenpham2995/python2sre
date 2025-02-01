import pytest
from list_manipulation import xor_list,and_list,left_list

a = [1, 2, 3]
b = [2, 4, 6]

def testXor():
    assert xor_list(a,b) == [1, 3, 4, 6]

def testAnd():
    assert and_list(a,b) == [2]
    
def testAndEmpty():
    a1 = []
    assert and_list(a1,b) == []

def testLeft():
    assert left_list(a,b) == [1, 3]