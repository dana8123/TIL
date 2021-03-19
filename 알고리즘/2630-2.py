n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

blue_count = 0
white_count = 0

# x,y,n 의 초기값 0,0,n
# graph[0][0]부터 시작해서, 정사각형 크기만큼 확인하는 함수
# for문 이하에서 x값과 y값 모두 확인하여 초기값과 같지않으면, check color에 -1을 반환하고 멈춘다.
# check color값을 확인하여 -1이면 종이를 반으로 나누고
# 초기값을 각각 네개로 나눈다.(x,y,n)(x,y+n,n)(x+n,y,n)(x+n,y+n,n)
# 나눈 초기값으로 다시 종이를 확인한다 (makepaper로 재귀)
# 만약 check != -1 이라면, 모든 종이의 색깔이 같으므로
# graph[x][y]의 값을 반환하여 색깔을 확인 후 카운트한다.


def makePaper(x, y, n):
    global blue_count, white_count

    check_color = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check_color != graph[i][j]:
                check_color = -1
                break

    if check_color == -1:
        n = n // 2
        makePaper(x, y, n)
        makePaper(x + n, y, n)
        makePaper(x, y + n, n)
        makePaper(x + n, y + n, n)
    elif check_color == 1:
        blue_count += 1
    elif check_color == 0:
        white_count += 1


makePaper(0, 0, n)
print(white_count)
print(blue_count)
