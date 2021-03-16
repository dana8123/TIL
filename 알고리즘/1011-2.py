case = int(input())

for i in range(case):
    x, y = map(int, input().split())
    distance = y - x
    count = 0
    same_count = 1
    while same_count < distance:  # 같은이동거리간의 합<길이 가 되면 count가 늘어남
        count += 1
        same_count += move  # count가 늘어난다는건 이동횟수도 1개 늘어난다는 뜻
        if count % 2 == 0:
            same_count += 1   # count가 짝수가 될 때 마다 시작값이 1씩 늘어나게됨.
    print(count)
