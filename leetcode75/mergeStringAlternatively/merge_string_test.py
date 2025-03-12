import pytest
from merge_string import merge_alternately

def testBothEmpty():
    assert merge_alternately("","") == ""

def testEmpty1():
    assert merge_alternately("","word2") == "word2"    

def testEmpty2():
    assert merge_alternately("word1","") == "word1"
    
def testSameLength():
    assert merge_alternately("abc","prg") == "apbrcg"
    
def testDiffLength():
    assert merge_alternately("ab","pqrs") == "apbqrs"
