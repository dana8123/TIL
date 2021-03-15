# 케이스 수 입력(삼각형 층수)
# list형태로 정수 입력
# 해당 값을 triangle list에 append
# triangle 내에서 각각의 배열에서 최대값 찾아 더하기..?
case = int(input())
triangle = []

for i in range(case):
    triangle.append(list(map(int, input().split())))

k = 2
for i in range(1, case):  # len은 0부터 안세니까. 0,1  [[1][1 2][1 2 3]]
    for j in range(k):
        if j == 0:  # 왼쪽 끝 값 일 때
          # 왼쪽 끝 값 = 바로 위에 있는 수를 더해서 나오는 값
            triangle[i][j] = triangle[i][j] + triangle[i-1][j]
        elif i == j:  # 오른쪽 끝 값
          # 자기 바로 대각선 위 값을 더해서 나오는 값
            triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
        else:  # 중간에 위치하는 값
            triangle[i][j] = max(triangle[i-1][j-1],
                                 triangle[i-1][j]) + triangle[i][j]

    k += 1

print(max(triangle[case-1]))
