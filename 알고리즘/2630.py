# 210318
# 백준 2630
# 1. 주어진 n만큼 입력하는 함수
# 1-1. 입력한 수를 전처리(이중배열 또는 리스트 형식)이중포문 채택..✅
# 2. n만큼이 전부 같은 숫자로 이루어져있는지 확인하는 함수
# 2-1. 0일 때, 1일 때 그 값을 카운트하는 행위 필요
# 3. n/2만큼 자르는 함수

case = int(input())
color_paper = []
for i in range(case):
    color_paper.append(list(map(int, input().split())))


def check(case, x: int, y: int) -> int::
    for i in range(case):
        for j in range(case):
            if sum(color_paper[i]) == case and sum(color_paper[i][j]) == case:
                blue += 1
            elif sum(color_paper[i]) == 0 and sum(color_paper[i][j]) == 0:
                white += 1
            else:
                return check(cut_paper(case),
# 1. 연속된 두 숫자가 다를경우 case//2한 후
# 2-1. 자른 종이 안에서 연속된 두 숫자가 다른지 확인
# 2. 다르다면 또다시 cut 함수 실행
# 3. 같다면 해당 종이의 색깔을 확인 후 카운트


def cut_paper(case):
    return case=case // 2
