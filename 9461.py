case = int(input())

memo = {
    1: 1,
    2: 1,
    3: 1
}  # memoization할 때 왜 세개를 미리 지정하냐면,
# 아래 식을 실행시키기위한 초기값이 필요하기 때문이다.
for i in range(1, 98):
    memo[i+3] = memo[i] + memo[i+1]  # 메모이제이션에 할당할 값을 계산해주고

for i in range(case):
    m = int(input())
    print(memo[m])  # 해당하는값이 있다면 프린트해준다.
