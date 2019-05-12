'''
В первой строке даны целое число 1 ≤ n ≤ 10**5
и массив A[1…n] из n различных натуральных чисел, не превышающих 10**9,
в порядке возрастания, во второй — целое число 1 ≤ k ≤ 10**5
и k натуральных чисел b1,…,bk, не превышающих 10**9.
Для каждого i от 1 до k необходимо вывести индекс 1 ≤ j ≤ n,
для которого A[j]=bi, или −1, если такого j нет.
'''
import sys
from bisect import bisect_left


def find_pos_by_hand(xs, query):
    # Invariant: lo <= pos < hi
    lo, hi = 0, len(xs)
    while lo < hi:
        mid = (lo + hi) // 2
        if query < xs[mid]:
            hi = mid  # [lo, mid)
        elif query > xs[mid]:
            lo = mid + 1  # [mid + 1, hi)
        else:
            return mid + 1  # 1-based index
    return -1


def find_pos_triv(xs, query):
    try:
        return xs.index(query) + 1
    except:
        return -1


def find_pos_bisect(xs, query):
    lo = bisect_left(xs, query)
    # i < lo : xs[i] < query
    # i >= lo : xs[i] >= query
    if lo < len(xs) and xs[lo] == query:
        return lo + 1
    return -1


def find_pos(xs, query, method='trivial'):
    if method == 'trivial':
        return find_pos_triv(xs, query)
    if method == 'hand':
        return find_pos_by_hand(xs, query)
    if method == 'bisect':
        return find_pos_bisect(xs, query)


def main():
    inp = sys.stdin
    reader = (map(int, line.split()) for line in inp)
    n, *xs = next(reader)
    k, *queries = next(reader)
    for query in queries:
        print(find_pos(xs, query), end=' ')


if __name__ == "__main__":
    main()
