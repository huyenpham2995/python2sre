import pytest
from check_strong_password import strongPassword

def testEmpty():
    assert strongPassword(0,"") == 6
    
def testMissing1():
    assert strongPassword(3,"Ab1") == 3

def testMissing2():
    assert strongPassword(11,"#HackerRank") == 1

def testSuccess():
    assert strongPassword(11,"2bb#Ah") == 0