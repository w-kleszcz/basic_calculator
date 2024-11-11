"""Modue implementing class with simple calculator operations"""

from math import nan

class Calculator:
    """Class implementing sum, subtractm multiply and divide operations"""
    def __init__(self, op1: float, op2: float):
        self.op1 = op1
        self.op2 = op2

    def sum(self):
        """Sum method."""
        return self.op1 + self.op2

    def subtract(self):
        """"Subtract method"""
        return self.op1 - self.op2

    def multiply(self):
        """Multiply method"""
        return self.op1 * self.op2

    def divide(self):
        """Divide method"""
        if self.op2 != 0.0:
            return self.op1 / self.op2

        return nan
