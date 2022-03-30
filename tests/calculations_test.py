"""Testing the Calculator with AAA"""

from calculator.Calculation import Addition, Subtraction, Multiplication, Division


def test_calculation_multiplication_instance():
    """Testing the Calculator multiplication"""
    # ARRANGE
    tuple_list = (1, 2)
    # ACT
    calculation = Multiplication.create(tuple_list)
    # ASSERT
    assert isinstance(calculation, Multiplication)


def test_calculation_subtraction_instance():
    """Testing the Calculator Subtract"""
    # ARRANGE
    tuple_list = (1, 2)
    # ACT
    calculation = Subtraction.create(tuple_list)
    # ASSERT
    assert isinstance(calculation, Subtraction)


def test_calculation_addition_instance():
    """Testing the Calculator addition"""
    # ARRANGE
    tuple_list = (1, 2)
    # ACT
    calculation = Addition.create(tuple_list)
    # ASSERT
    assert isinstance(calculation, Addition)


def test_calculation_add_get_result_method():
    """Testing the Calculator"""
    # ARRANGE
    tuple_list = (1, 2)
    # ACT
    calculation = Addition.create(tuple_list)
    # ASSERT
    assert calculation.get_result() == 3


def test_calculation_subtract_get_result_method():
    """Testing the Calculator Subtract"""
    # ARRANGE
    tuple_list = (1, 2)
    # ACT
    calculation = Subtraction.create(tuple_list)
    # ASSERT
    assert calculation.get_result() == -1


def test_calculation_multiply_get_result_method():
    """Testing the multiplication"""
    # ARRANGE
    tuple_list = (1, 2)
    # ACT
    calculation = Multiplication.create(tuple_list)
    # ASSERT
    assert calculation.get_result() == 2


def test_calculation_division_get_results_method():
    """Testing the calculator division"""
    # ARRANGE
    tuple_list = (1, 2)
    # ACT
    calculation = Division.create(tuple_list)
    # ASSERT
    assert calculation.get_result() == 0.5
