from collections import Counter
case = int(input())
num = []
for i in range(case):
    num.append(int(input()))
num.sort()


def avg(num):
    result = sum(num) // case
    return result


def mid(num):
    if case == 1:
        return num[0]
    else:
        if case % 2 != 0:  # 홀수일 때
            return (num[case//2])  # num의 가운데 값
        else:
            return (round((num[case//2]) + (num[case//2 + 1])/2))


def many(num):
    if n == 1:
        return num[0]
    c = Counter(num).most_common(2)


def rangeOf(num):
    return num[case - 1] - num[0]


print(avg(num))
print(mid(num))
print(rangeOf(num))
