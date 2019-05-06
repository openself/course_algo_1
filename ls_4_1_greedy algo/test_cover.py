from cover_segment_with_points import cover


def test_case_1():
    data = [
        (1, 3),
        (2, 5),
        (3, 6)
    ]

    assert cover(data) == [3]

def test_case_2():
    data = [
        (4, 7),
        (1, 3),
        (2, 5),
        (5, 6)
    ]

    assert cover(data) == [3, 6]