from bin_search import find_pos

def test_case_1():
    array = [1, 5, 8, 12, 13]
    queries = [8, 1, 23, 1, 11]
    ouput = list()
    for query in queries:
        ouput.append(find_pos(array, query, 'bisect'))

    assert ouput == [3, 1, -1, 1, -1]

def test_case_2():
    assert find_pos([], 42, 'bisect') == -1
    assert find_pos([42], 42, 'bisect') == 1
    assert find_pos([42], 24, 'bisect') == -1