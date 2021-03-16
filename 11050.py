case = int(input())
for i in range(case):
    n, m = map(int, input().split())


def factorial(a):
    if a > 1:
        return a * factorial(a-1)
    return 1


def binal(n, m):
    return factorial(m) // (factorial(n)*factorial(m-n))


print(binal(n, m))
