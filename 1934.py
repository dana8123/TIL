case = int(input())
for i in range(case):
    num = list(map(int, input().split()))
    a, b = num[0], num[1]
    while b != 0:
        a = a % b
        a, b = b, a

    print(num[0] * num[1] // a)
