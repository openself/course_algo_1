'''
Первая строка содержит число 1 ≤ n ≤ 10**5,
вторая — массив A[1…n], содержащий натуральные числа, не превосходящие 10**9.
Необходимо посчитать число пар индексов 1 ≤ i < j ≤ n, для которых A[i] > A[j].
(Такая пара элементов называется инверсией массива.)

Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности:
например, в упорядоченном по неубыванию массиве инверсий нет вообще,
а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.
'''
import sys


def count_inversions(xs):
    '''
    Деревья с двоичным индексом - используются для поддержания префиксных сумм
    по значениям элементов перестановки. Затем можно просто перейти справа налево
    и подсчитать для каждого элемента количество элементов меньше, чем справа.
    Сложность O(n * log n), а постоянный коэффициент очень низок.
    https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/
    '''
    res = 0
    counts = [0] * (len(xs) + 1)
    rank = {v: i + 1 for i, v in enumerate(sorted(xs))}
    for x in reversed(xs):
        i = rank[x] - 1
        while i:
            res += counts[i]
            i -= i & -i
        i = rank[x]
        while i <= len(xs):
            counts[i] += 1
            i += i & -i
    return res


def main():
    inp = sys.stdin
    reader = (map(int, line.split()) for line in inp)
    n = next(reader)
    xs = list(next(reader))
    print(count_inversions(xs))


if __name__ == "__main__":
    main()
