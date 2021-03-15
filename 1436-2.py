n = int(input())  # 스트링으로 받아지나..?ㄴ
count = 0
six_n = 666
while True:
    if '666' in str(six_n):
        count += 1
    if count == n:
        print(six_n)
        break
    else:
        six_n = six_n + 1
