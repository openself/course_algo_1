def fib_digit(n):
    '''
    Дано число 1 ≤ n ≤ 10**7, необходимо найти последнюю цифру n-го числа Фибоначчи.
    Как мы помним, числа Фибоначчи растут очень быстро, поэтому при их вычислении
    нужно быть аккуратным с переполнением. В данной задаче, впрочем, этой проблемы
    можно избежать, поскольку нас интересует только последняя цифра числа Фибоначчи:
    если 0 ≤ a, b ≤ 9 — последние цифры чисел Fi и Fi+1 соответственно, то
    (a + b) mod 10 — последняя цифра числа Fi+2.
    '''
    if n < 2:
        return n
    else:
        fib_digit_prev = 0
        fib_digit_last = 1
        for i in range(2, n):
            fib_digit_last, fib_digit_prev = (fib_digit_last + fib_digit_prev) % 10,  fib_digit_last
        return (fib_digit_last + fib_digit_prev) % 10

def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()