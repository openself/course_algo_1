def fib_mod(n, m):
    '''
    Даны целые числа 1 ≤ n ≤ 10**18 и 2 ≤ m ≤ 10**5,
    необходимо найти остаток от деления n-го числа Фибоначчи на m.
    '''
    fib_prev = 0
    fib_last = 1
    cached = [fib_prev, fib_last]
    for i in range(1, n):
        fib_last, fib_prev = (fib_last + fib_prev) % m, fib_last
        if fib_prev == 0 and fib_last == 1:
            cached.pop()
            break
        else:
            cached.append(fib_last)

    offset = n % len(cached)
    return cached[offset]

def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()