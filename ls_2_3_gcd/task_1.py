def gcd(a, b):
    assert 0 <= a <= 2e9
    assert 0 <= b <= 2e9
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return gcd(a % b, b)
    else:
        return gcd(a,  b % a)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()