from collections import deque

green_tomato = deque()


def tomato(tomato_array, start_tomato):
    red_tomato = []
    green_tomato = [start_tomato]
    while green_tomato:
        current_tomato = green_tomato.pop()
        red_tomato.append(current_tomato)
        day = 0
        for near_tomato in tomato_array[current_tomato]:
            if near_tomato not in red_tomato:
                red_tomato.append()
                day += 1
    return red_tomato


# dict 생성하기 (토마토바구니..? 하..너무싫어 토마토 극혐)
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
box = {

}
