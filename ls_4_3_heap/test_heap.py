import heapq
from heap import process_command

def test_case_1():
    maxh = list()
    test_list = [
        'Insert 200',
        'Insert 10',
        'Insert 5',
        'Insert 500',
        'ExtractMax',
        'ExtractMax',
        'ExtractMax',
        'ExtractMax',
    ]
    output_list = list()

    for data_string in test_list:
        data = data_string.split()
        command = None
        value = None

        if len(data) == 2:
            command, value = data
        elif len(data) == 1:
            command = data[0]

        output = process_command(maxh, command, value)
        output_list.append(output)

    assert output_list == [
        None, None, None, None, 500, 200, 10, 5
    ]


def test_case_2():
    maxh = list()
    test_list = [
        'Insert 2',
        'Insert 3',
        'Insert 15',
        'Insert 18',
        'Insert 12',
        'ExtractMax',
        'ExtractMax',
        'ExtractMax',
    ]
    output_list = list()

    for data_string in test_list:
        data = data_string.split()
        command = None
        value = None

        if len(data) == 2:
            command, value = data
            value = int(value)
        elif len(data) == 1:
            command = data[0]

        output = process_command(maxh, command, value)
        output_list.append(output)

    assert output_list == [
        None, None, None, None, None, 18, 15, 12
    ]
