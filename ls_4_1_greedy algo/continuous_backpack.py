'''
Непрерывный рюкзак
Первая строка содержит количество предметов 1≤ n ≤ 10**3 и вместимость рюкзака 0 ≤ W ≤ 2⋅*10**6.
Каждая из следующих n строк задаёт стоимость 0 ≤ ci ≤ 2 *⋅10**6
и объём 0 < wi ≤ 2 *⋅10**6 предмета (n, W, ci, wi — целые числа).
Выведите максимальную стоимость частей предметов
(от каждого предмета можно отделить любую часть, стоимость и объём при этом
пропорционально уменьшатся), помещающихся в данный рюкзак,
с точностью не менее трёх знаков после запятой.
'''

import sys


def pack(total_vol, s):
    if not s:
        return ""

    s.sort(key=lambda tup: tup[0]/tup[1], reverse=True)

    sum = 0
    cur_vol = 0

    for item in s:
        cost, vol = item
        cost_per_vol = cost / vol
        if vol + cur_vol > total_vol:
            vol = total_vol - cur_vol
        sum += vol * cost_per_vol

        cur_vol += vol
        if cur_vol == total_vol:
            break

    return round(sum, 3)


def main():
    s = list()
    inp = sys.stdin
    n, v = map(int, inp.readline().split())
    for _ in range(n):
        s.append(tuple(map(int, inp.readline().split())))

    print('%.3f' % pack(v, s))


if __name__ == "__main__":
    main()