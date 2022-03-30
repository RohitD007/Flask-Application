"""Testing the Calculator"""
from calculator import Calculator


def test_calculator_add_method():
    """Testing the Calculator Addition"""
    # ARRANGE
    tuple_list = (1.0, 2.0)
    # ACT
    result = Calculator.add(tuple_list)
    # ASSERT
    assert result == 3.0


def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    # ARRANGE
    tuple_list = (1.0, 2.0)
    # ACT
    result =  Calculator.subtract(tuple_list)
    # ASSERT
    assert result == -1.0


def test_calculator_multiply_method():
    """Testing the Calculator Multiply"""
    # ARRANGE
    tuple_list = (1.0, 2.0)
    # ACT
    result = Calculator.multiply(tuple_list)
    # ASSERT
    assert result   == 2.0


def test_calculator_divide_method():
    """ Testing the calculator division"""
    # ARRANGE
    tuple_list = (1.0, 2.0)
    # ACT
    result = Calculator.divide(tuple_list)
    # ASSERT
    assert result == 0.5
