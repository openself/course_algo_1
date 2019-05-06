import unittest
from ls_2_2_Fibo.task_2 import fib_digit

class Case1(unittest.TestCase):
    def test_1(self):
        n = 2
        fib_number = fib_digit(n)
        self.assertEqual(fib_number, 1)

    def test_2(self):
        n = 317457
        fib_number = fib_digit(n)
        self.assertEqual(fib_number, 2)

if __name__ == '__main__':
	unittest.main(verbosity=2)