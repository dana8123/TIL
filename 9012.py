# 21.03.16
# 백준 9012번
# (의 경우 count에서 +1
# )의 경우 count에서 -1
# 하여 count가 0이 될 때만 yes를 출력하되
# ())(() 의 경우 count= 0이지만, vps가 아니다.
# 따라서 ()) 의 경우 -1을 print하는 식인, count = -1일 때의 경우를 추가한다.
case = int(input())

for i in range(case):
    vps = input()
    vpslist = list(vps)
    count = 0
    for i in vpslist:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count == -1:
            print("NO")
            break
    if count > 0:
        print("NO")
    elif count == 0:
        print("YES")
