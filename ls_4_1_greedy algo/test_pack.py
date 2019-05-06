from continuous_backpack import pack


def test_case_1():
    v = 50
    s = [
        (60, 20),
        (100, 50),
        (120, 30),
    ]

    assert pack(v, s) == 180