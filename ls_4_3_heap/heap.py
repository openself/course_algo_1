'''
Первая строка входа содержит число операций 1 ≤ n ≤ 10**5.
Каждая из последующих n строк задают операцию одного из следующих двух типов:
 * Insert x, где 0 ≤ x ≤ 10**9 — целое число;
 * ExtractMax
Первая операция добавляет число x в очередь с приоритетами,
вторая — извлекает максимальное число и выводит его.
'''
import sys
import heapq


def process_command(maxh, command, value):
    output = None
    if command == 'Insert':
        heapq.heappush(maxh, -value)

    if command == 'ExtractMax':
        output = - heapq.heappop(maxh)

    return output


def main():
    maxh = list()

    inp = sys.stdin
    n = int(inp.readline())
    for _ in range(n):
        data = inp.readline().split()
        command = None
        value = None

        if len(data) == 2:
            command, value = data
            value = int(value)
        elif len(data) == 1:
            command = data[0]

        output = process_command(maxh, command, value)
        if output:
            print(output)


if __name__ == "__main__":
    main()
