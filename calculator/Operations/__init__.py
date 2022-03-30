""" These are the Operation Classes"""


class Addition:
    """ This is the addition class"""

    @staticmethod
    def add(value_1, value_2):
        """ This is the add method"""
        return value_1 + value_2


class Subtraction:
    """ This is the subtraction class"""

    @staticmethod
    def subtract(value_1, value_2):
        """ This is the subtract method"""
        return value_1 - value_2


class Multiplication:
    """ This is the multiplication class"""

    @staticmethod
    def multiply(value_1, value_2):
        """ This is the multiply method"""
        return value_1 * value_2


class Division:  # pylint: disable=too-few-public-methods
    """ This class is used for division of 2 numbers"""

    @staticmethod
    def divide(value_1, value_2):
        """This method does the division operation"""
        try:
            result = value_1 / value_2
            return result
        except ZeroDivisionError:
            print("You can't divide by zero!")
