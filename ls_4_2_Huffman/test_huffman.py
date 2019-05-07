from huffman_algo import encode, output_encoded_result


def test_case_1():
    data = 'a'
    result = ['1 1',
              'a: 0',
              '0']
    assert output_encoded_result(data, encode(data)) == result

def test_case_2():
    data = ''
    result = ['0 0',
              '']
    assert output_encoded_result(data, encode(data)) == result

def test_case_3():
    data = 'abacabad'
    result = ['4 14',
              'a: 0',
              'b: 10',
              'c: 110',
              'd: 111',
              '01001100100111']
    code = encode(data)
    assert output_encoded_result(data, code) == result

def test_case_4():
    data = 'aaaaa'
    result = ['1 5',
              'a: 0',
              '00000']
    code = encode(data)
    assert output_encoded_result(data, code) == result