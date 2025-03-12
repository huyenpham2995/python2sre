import pytest
from reverseList import reverseListOne, reverseListTwo

def testEmpty():
    assert reverseListOne([]) == []
    assert reverseListTwo([]) == []

def testOneElement():
    assert reverseListOne([1]) == [1]
    assert reverseListTwo([1]) == [1]

def testOddList():
    assert reverseListOne([1,2,3,4,5]) == [5,4,3,2,1]
    assert reverseListTwo([1,2,3,4,5]) == [5,4,3,2,1]

def testEvenList():
    assert reverseListOne([1,2,3,4,5,6]) == [6,5,4,3,2,1]
    assert reverseListTwo([1,2,3,4,5,6]) == [6,5,4,3,2,1]