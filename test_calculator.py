"""Calculator class test"""
from math import nan
from calculator import Calculator

class TestClass:
    """Test class"""
    def test_sum(self):
        """Test sum"""
        calc = Calculator(2.0, 2.0)
        assert calc.sum() == 4.0

    def test_subtract(self):
        """Test subtract"""
        calc = Calculator(4.0, 2.0)
        assert calc.subtract() == 2.0

    def test_multiply(self):
        """Test multiply"""
        calc = Calculator(2.0, 3.0)
        assert calc.multiply() == 6.0

    def test_division(self):
        """Test divide"""
        calc = Calculator(4.0, 2.0)
        assert calc.divide() == 2.0
        calc = Calculator(1.0, 0.0)
        assert calc.divide() is nan
