import pytest
from can_place_flowers import can_place_flowers

def testOneFlowerOneSlot():
    assert can_place_flowers([1],n=1) == False
    assert can_place_flowers([1],n=0) == True
    
def testNoFlowerOneSlot():
    assert can_place_flowers([0],n=1) == True
    assert can_place_flowers([0],n=0) == True

def testMultipleFlowersMultipleSlots():
    assert can_place_flowers([1,0,0,0,1],n=1) == True
    assert can_place_flowers([1,0,0,0,1],n=2) == False