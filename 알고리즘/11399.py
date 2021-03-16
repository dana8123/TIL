case = int(input())
time = list(map(int, input().split()))
long = 0

time.sort()

for i in range(case):  # 0,1,2,3,4
    for j in range(i+1):  # 1,2,3,4,5
        long += time[j]
        # 총 걸린 시간 = (1번사람이 인출)+(1번인출,2번인출)....


print(long)
