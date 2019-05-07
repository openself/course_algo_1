'''
По данной непустой строке s длины не более 10**4, состоящей из строчных букв латинского алфавита,
постройте оптимальный беспрефиксный код. В первой строке выведите количество различных букв k,
встречающихся в строке, и размер получившейся закодированной строки.
В следующих k строках запишите коды букв в формате "letter: code".
В последней строке выведите закодированную строку.
'''
from collections import Counter
import heapq

def encode(data):
    code = dict()
    if not data:
        return code
    elif len(data) == 1:
        return {data: '0'}

    heap_data = list()

    for char, freq in Counter(data).items():
        heap_data.append((freq, len(heap_data), char))
        heapq.heapify(heap_data)

    count = len(heap_data)
    # if count == 1:
    #     return dict(Counter(data))

    while len(heap_data) > 1:
        freq1, _count1, left = heapq.heappop(heap_data)
        freq2, _count2, right = heapq.heappop(heap_data)
        heapq.heappush(heap_data, (freq1 + freq2, count, {'0': left, '1': right}))
        count += 1

    [(_freq, count, root)] = heap_data
    if count == 0:
        return {root: '0'}

    walk(code, '', root)
    return code

def walk(code, acc, node, side=''):
    if not side:
        walk(code, acc, node, '0')
        walk(code, acc, node, '1')
        return code

    try:
        node = node[side]
    except:
        node = None

    if not node:
        return code

    acc += side
    if len(node) == 1:
        code[node] = acc
        return code
    else:
        walk(code, acc, node)


def output_encoded_result(source, code):
    encoded = ''.join(code[char] for char in source)
    answer = [f'{len(code)} {len(encoded)}']
    for char in sorted(code):
        answer.append(f'{char}: {code[char]}')
    answer.append(encoded)

    return answer

def main():
    data = input()
    code = encode(data)
    result = output_encoded_result(data, code)
    for s in result:
        print(s)


if __name__ == "__main__":
    main()
