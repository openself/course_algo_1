def fib(n):
    '''
    Дано целое число 1 ≤ n ≤ 40, необходимо вычислить n-е число Фибоначчи
    (напомним, что F0=0, F1=1 и Fn = Fn−1 + Fn−2 при n ≥ 2).
    '''
    if n < 2:
        return n
    else:
        fib_prev = 0
        fib_last = 1
        for i in range(2, n):
            fib_last, fib_prev = fib_last + fib_prev, fib_last
        return fib_last + fib_prev

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()