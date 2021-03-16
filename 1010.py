n, k = map(int, input().split())


def factorial(a):
    if a > 1:
        return a * factorial(a-1)
    return 1


def binal(n, k):
    return factorial(n) // (factorial(k)*factorial(n-k))


print(binal(n, k))
