def prime(x):
    for i in range(2, int(x ** 0.5)+1):
        if x % i == 0:
            return False
    return x != 1


a, b = map(int, input().split())

for i in range(int(a), int(b)+1):
    if prime(i) == True:
        print(i)
