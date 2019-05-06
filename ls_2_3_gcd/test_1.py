from ls_2_3_gcd.task_1 import gcd


def test_case_1():
    m = 18
    n = 35
    assert gcd(m, n) == 1


def test_case_2():
    m = 14159572
    n = 63967072
    assert gcd(m, n) == 4


def test_case_3():
    m = 99999999
    n = 99999999
    assert gcd(m, n) == 99999999