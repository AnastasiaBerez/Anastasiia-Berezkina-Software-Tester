import pytest
from sum import calculate_sum

def test_calculate_sum():
    assert calculate_sum(10, 5) == 15
    assert calculate_sum(2,20) == 22

def test_calculate_sum_negative():
    assert calculate_sum(10, -5) == 5
    assert calculate_sum(2,-20) == -18

def test_calculate_sum_zero():
    assert calculate_sum(10, 0) == 10
    assert calculate_sum(0,20) == 20

def test_calculate_sum_float():
    assert calculate_sum(10.5, 5.3) == 15.8
    assert calculate_sum(2.2, 20) == 22.2

def test_calculate_sum_exeption1():
    with pytest.raises(TypeError):
        calculate_sum("r", 6)
        calculate_sum(5,"%")
        calculate_sum("#","%")