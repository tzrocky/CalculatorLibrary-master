"""Unit tests for the calculator library."""


import calculator


class TestCalculator:

    def test_addition(self):
        """Check the sum of first and second params."""
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        """Check the substract of first and second params."""
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        """Check the product of first and second params."""
        assert 100 == calculator.multiply(10, 10)
