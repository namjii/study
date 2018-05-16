import unittest

from data_structure2.Fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        assert fibonacci(1) == 0
        assert fibonacci(2) == 1
        assert fibonacci(3) == 1
        assert fibonacci(4) == 2
        assert fibonacci(5) == 3
        assert fibonacci(6) == 5
        assert fibonacci(10) == 34, fibonacci(10)
