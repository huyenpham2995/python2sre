import pytest
from piling_up import piling_up

def testEmpty():
    assert piling_up([]) == "Yes"
    
def testYes():
    assert piling_up([1,2,3,7,8]) == "Yes"
    assert piling_up([4, 3, 2, 1, 3, 4]) == "Yes"

def testNo():
    assert piling_up([1,2,3,8,7]) == "No"
    assert piling_up([1, 3, 2]) == "No"

