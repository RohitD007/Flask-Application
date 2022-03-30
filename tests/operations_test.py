"""Testing the calculator operations """

from calculator.Operations import Addition, Subtraction, Multiplication, Division


def testing_operations_add():
    """Testing the Calculator"""
    assert Addition.add(3, 3) == 6


def testing_operations_subtract():
    """Testing the Calculator"""
    assert Subtraction.subtract(3, 2) == 1


def testing_operations_multiply():
    """Testing the Calculator"""
    assert Multiplication.multiply(2, 2) == 4


def testing_operations_divide():
    """Testing the Calculator"""
    assert Division.divide(1, 2) == 0.5


def testing_operations_divide_by_zero():
    """Testing the Divide By Zero operation"""
    try:
        Division.divide(1, 0)
    except ZeroDivisionError:
        assert True
