from huffman_algo import encode


def test_case_1():
    data = 'a'
    result = ['1 1',
              'a: 0',
              '0']
    assert encode(data) == result

def test_case_2():
    data = 'abacabad'
    result = ['4 14',
              'a: 0',
              'b: 10',
              'c: 110',
              'd: 111',
              '01001100100111']

    assert encode(data) == result