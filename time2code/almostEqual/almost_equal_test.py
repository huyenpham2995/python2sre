import pytest
from almost_equal import is_almost_equal

def testEmpty():
    assert is_almost_equal('x','') == True
    
def testTrue():
    assert is_almost_equal('xyz','xyc') == True
    assert is_almost_equal('xyz','xy') == True
    assert is_almost_equal('xyz','xz') == True
    assert is_almost_equal('xyz','yz') == True
    assert is_almost_equal('xyz','xyzz') == True
    assert is_almost_equal('xyz','xayz') == True
    
def testFalse():
    assert is_almost_equal('xyz','xyz') == False
    assert is_almost_equal('xyz','xzy') == False
    assert is_almost_equal('xyz','xk') == False
    assert is_almost_equal('xyz','yzxtxy') == False