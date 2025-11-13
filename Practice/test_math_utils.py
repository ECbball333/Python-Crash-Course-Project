import pytest
from math_utils import add, safe_div

def test_add():
    assert add(3,5) == 8

def test_safe_div_ok():
    assert safe_div(10,2) == 5

def test_safe_div_raise():
    with pytest.raises(ZeroDivisionError):
        safe_div(1,0)

