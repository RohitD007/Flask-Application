"""Calculation History Class"""
from calculator.Calculation import Addition, Subtraction, Multiplication, Division


class Calculation:
    """Calculation class manages the History of Calculation"""
    history = []

    @staticmethod
    def clear_history():
        """clear the History of Calculation"""
        Calculation.history.clear()
        return True

    @staticmethod
    def count_history():
        """get number of items in History"""
        return len(Calculation.history)

    @staticmethod
    def get_last_calculation_object():
        """get last calculation"""
        return Calculation.history[-1]

    @staticmethod
    def get_last_calculation_result_value():
        """get last calculation"""
        calculation = Calculation.get_last_calculation_object()
        return calculation.get_result()

    @staticmethod
    def get_first_calculation():
        """get first calculation"""
        return Calculation.history[0]

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from History"""
        return Calculation.history[num]

    @staticmethod
    def add_calculation(calculation):
        """ get a generic calculation from History"""
        return Calculation.history.append(calculation)

    @staticmethod
    def add_addition_calculation(values):
        """Create an addition and add object to History using factory method create"""
        Calculation.add_calculation(Addition.create(values))
        return True

    @staticmethod
    def add_subtraction_calculation(values):
        """Create a subtraction object to History using factory method create"""
        Calculation.add_calculation(Subtraction.create(values))
        return True

    @staticmethod
    def add_multiplication_calculation(values):
        """Create multiplication object to History using factory method create"""
        Calculation.add_calculation(Multiplication.create(values))
        return True

    @staticmethod
    def add_division_calculation(values):
        """Create division object to History using factory method create"""
        Calculation.add_calculation(Division.create(values))
        return True
