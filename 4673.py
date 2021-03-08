generate_num = []
natural_num = list(range(1, 10001))


def d(n):                 # n = 33 일 때
    num = list(str(n))     # num = ['3', '3']
    dnum = 0
    # i = [0, 1] len(num)은 intiger라 for문에 쓸 수 없음, range 사용
    for i in range(len(num)):
        dnum += int(num[i])    # dnum = 0 + 3 + 3
    return n + dnum         # d(n) = 33+ 3 + 3


for i in natural_num:
    generate_num.append(d(i))

for j in natural_num:           # j = [1,2,3, ... , 10000]
    if j in generate_num:
        continue
    else:
        print(j)
