import pytest
from largest_number_of_candies import kids_with_candies

def testCandies1():
    assert kids_with_candies([2,3,5,1,3],3) == [True,True,True,False,True]

def testCandies2():
    assert kids_with_candies([4,2,1,1,2],1) == [True,False,False,False,False]

def testCandies3():
    assert kids_with_candies([12,1,12],10) == [True,False,True]
