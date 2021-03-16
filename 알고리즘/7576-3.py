from collections import deque

w, h = map(int, input().split())  # 넓이와 높이를 입력받음
maps = [list(map(int, input().split()))
        for _ in range(h)]  # 높이만큼의 반복문을 돌면서 []를 반복적으로 입력받음
day = 0
move_x = [0, 0, -1, +1]
move_y = [-1, 1, 0, 0]  # x,y를 상하좌우로 한칸씩 움직이게 하기위한 사전작업


tomatos = deque()

for i in range(h):  # 높이만큼
    for j in range(w):  # 높이만큼 넓이 만큼
        if tomato_point[i][j] == 1:  # 좌표값이 1인곳을 찾아
            tomatos.append([i, j])  # tomatos라는 queue에 넣어. 얘가 초기값. start_node?


def tomato():
    red_tomato = []
    # tomatos = [tomato_point]  # 결국 토마토포인트는 좌표값(x,y)가 필요한거였음; 그래서 위에서 설정해줌.
    while tomatos:
        tomato_x, tomato_y = tomatos.popleft()   # tomato_x에는 x좌표, y에는 y 좌표 들어감(시작점)
        # current_tomato = tomatos.pop()   좌표값이 필요해서 이건 폐기
        # red_tomato.append(current_tomato)  마찬가지의 이유로 폐기 이런 초기설정 필요없음
        for near_tomato in range(4):  # 토마토포인트를 for문 돌려줌(상,하,좌,우)
            ripe_x = tomato_x + move_x[near_tomato]  # 토마토 좌표를 움직여준다.
            ripe_y = tomato_y + move_y[near_tomato]  #
            # 익은 토마토의 좌표가 상자의 규격을 벗어나지 않고, 안익은 토마토일 때
            if 0 <= ripe_x <= h and 0 <= ripe_w <= h and tomato_point[ripe_x][ripe_y] == 0:
                tomato_point[ripe_x][ripe_y] = tomato_point[tomato_x][tomato_y]
                # 익은 토마토들의 좌표를 추가한다 // 하루는 언제 더해줘?
                red_tomato.append([ripe_x, ripe_y])
    return red_tomato

# 좌표 전체를 돌면서 0을 찾아 반환하고 날짜를 계산하는 함수


def howLong():
    ans = 0
    for i in range(h):
        for j in range(W):
            a = maps[i][j]  # 전체 좌표
            if 0 == a:
                print(-1)
              return
            ans = max(a)     #좌표 내 익ㅇ지않은 토마토가 없을 때, 좌표 내 가장 큰 값( 즉 마지막 좌표 )
        print(ans)      
