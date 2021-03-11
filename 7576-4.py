import sys
from collections import deque
input = sys.stdin.readline

w, h = map(int, input().split())
tomato_point = [list(map(int, input().split()))
                for _ in range(h)]  # 높이만큼의 반복문을 돌면서 []를 반복적으로 입력받음
day = 0
move_x = [-1, 1, 0, 0]
move_y = [0, 0, 1, -1]  # x,y를 상하좌우로 한칸씩 움직이게 하기위한 사전작업


tomatos = deque()

for i in range(h):  # 높이만큼
    for j in range(w):  # 높이만큼 넓이 만큼
        if tomato_point[i][j] == 1:  # 좌표값이 1인곳을 찾아
            tomatos.append([i, j])  # tomatos라는 queue에 넣어. 얘가 초기값. start_node?


def tomato():
    global toamtos
    while tomatos:
        tomato_x, tomato_y = tomatos.popleft()
        for i in range(4):  # 상,하,좌,우 로 모두 움직임. i=1 상, 2 하...
            ripe_x = tomato_x + move_x[i]
            ripe_y = tomato_y + move_y[i]
            if 0 <= ripe_x < h and 0 <= ripe_y < w and tomato_point[ripe_x][ripe_y] == 0:
                # 다음 좌표에 1로 저장하고,
                tomato_point[ripe_x][ripe_y] = tomato_point[tomato_x][tomato_y] + 1
                tomatos.append([ripe_x, ripe_y])  # 큐에 x,y 값 넣어줌


def howLong():
    ans = 0
    for i in range(h):
        for j in range(w):
            a = tomato_point[i][j]  # 전체 좌표
            if 0 == a:
                print(-1)
                return
            ans = max(ans, a)  # 좌표 내 익ㅇ지않은 토마토가 없을 때, 좌표 내 가장 큰 값( 즉 마지막 좌표 )
    print(ans - 1)


tomato()
howLong()
