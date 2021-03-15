n = int(input())  # 집의 개수
p = []
for i in range(n):
  # 집의 개수만큼 list안에 가격list 생성(2차원배열)
  # [[12,20,31][13,15,28][26,10,11]]
    p.append(list(map(int, input().split())))
  # 집의 개수만큼 1부터 for문을 돌려줌
  # i번째 집에서 해당하는 경우의 수를 모두 저장(i번째와 i+1번째)
  # 연속된 색상이 걸리는 경우는 없으므로, R이 첫번째일 때, G가 첫번째 일 때.
  # B가 첫번째 일 때의 경우를 모두 P list에 저장함
  # [[R이 맨 앞일 때 최소값][G가 맨 앞일 때 최소값][B가 맨 앞일 때 최소값]] 마지막집의 모든 경우의 수가 끝날 때 까지 계산
  # p = [[(1번째집 R로 시작할 때),(1 G)(1 B)][(2번째집의 R)(2 G)(2 B)][(3번째집의 R)(3 G)(3 B)]]]
for i in range(1, len(p)):
    p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]  # i번째 집 R이 처음
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]  # i번째 집 G가 처음
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]  # i번째 집 B가 처음
    print(p)
# 위에서 구했던 세가지?? 경우의 수 중,가장 작은값은 프린트
# 이중배열의 두번째 list중 가장 작은값을 찾는 과정
# [[26, 40, 83], [89, 86, 83], [96, 172, 185]] 중 가장 작은값 찾기
# 이중배열의 최소값 찾기
print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))
print(p)