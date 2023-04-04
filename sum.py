import pytest

def calculate_sum(a, b):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        raise TypeError("Вхожные данные должны быть числами")
    return a+b



def test_calculate_sum_exeption1():
    with pytest.raises(TypeError):
        calculate_sum("r", 6)
        calculate_sum(5,"%")
        calculate_sum("#","%")

