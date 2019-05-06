import unittest
from ls_2_2_Fibo.task_1 import fib

class Case1(unittest.TestCase):
    def test_1(self):
        n = 3
        fib_number = fib(n)
        self.assertEqual(fib_number, 2)
    def test_2(self):
        n = 21
        fib_number = fib(n)
        self.assertEqual(fib_number, 10946)

if __name__ == '__main__':
	unittest.main(verbosity=2)