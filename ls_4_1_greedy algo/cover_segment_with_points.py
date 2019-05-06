'''
По данным n отрезкам необходимо найти множество точек минимального размера,
для которого каждый из отрезков содержит хотя бы одну из точек.

В первой строке дано число 1 ≤ n ≤ 100 отрезков.
Каждая из последующих n строк содержит по два числа 0 ≤ l ≤ r ≤ 10**9,
задающих начало и конец отрезка.
Выведите оптимальное число m точек и сами m точек.
Если таких множеств точек несколько, выведите любое из них.
'''

import sys
from operator import itemgetter

def cover(s):
    if not s:
        return s

    s.sort(key=itemgetter(1))
    answer = list()
    point_prev = None

    for i in range(len(s)):
        if point_prev == None:
            point_prev = point = s[i][1]
            answer.append(point_prev)
        point = s[i][0]
        if point <= point_prev:
            continue
        else:
            point_prev = s[i][1]
            answer.append(point_prev)



    return answer


def main():
    s = list()
    inp = sys.stdin
    n = int(inp.readline())
    for _ in range(n):
        s.append(tuple(map(int, inp.readline().split())))
    answer = cover(s)
    print(len(answer))
    print(" ".join(map(str, answer)))


if __name__ == "__main__":
    main()