n = int(input())
count = 0
six_n = 666
while True:
    if '666' in str(six_n):  # if in 은 string만 비교
        count += 1  # 아래 if 하위 수준이 아닌 이유:
        # 하위수준일 경우, 1번 조건이 무한반복되기 때문에 하위로 안내려옴
        # and를 쓸 경우, 둘 다 만족해야해서 count=n인 경우가 0제외하고 충족안됨
        # or쓸 경우, 계속 666이 있기 때문에 무한반복됨
        # 그래서 if문을 동일수준으로 두개 만들어야함.
    if count == n:
        print(six_n)
        break  # 브레이크없으면 무한반복
    else:
        six_n = six_n + 1  # 666,667,668,669,...1666,1667,1668...
