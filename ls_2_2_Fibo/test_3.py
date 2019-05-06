from ls_2_2_Fibo.task_3 import fib_mod


def test_1():
    n = 10
    m = 2
    mod = fib_mod(n, m)
    assert mod == 1

def test_2():
    n = 1000000000001
    m = 99999
    mod = fib_mod(n, m)
    assert mod == 63715

def test_3():
    n = 100000000000000000000000000001
    m = 10000
    mod = fib_mod(n, m)
    assert mod == 7501