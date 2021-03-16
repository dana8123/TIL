# 21.03.16
# 백준 10773
# case 만큼 for 아래의 코드를 실행한다.
# 만약 입력받은 숫자가 0이 아니라면 zero에 추가하고
# 0이라면 zero.pop() 한다.
# 최종값은 리스트의 합을 구한다.
case = int(input())
zero = []
for i in range(case):
    num = int(input())
    if num != 0:
        zero.append(num)
    else:
        zero.pop()
print(sum(zero))
