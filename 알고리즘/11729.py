n = int(input())


def hanoi(n, frm, via, to):
    if n == 1:   # 가장 큰 원반이 to로 옮겨지고, 동시에 나머지 원반들이 via로 옮겨감
        print(frm, to)
        return
    else:
        hanoi(n-1, frm, to, via)
        print(frm, to)  # 가장 작은 원반이 다른곳으로 옮겨짐 , 나머지원반이 frm에 남음
        # frm에 있는 원반이 또 다른곳으로 옮겨짐, 가장 큰 원반 빼고
        hanoi(n-1, via, to, frm)  # via 는 2개의 원반이 있는 상태


hanoi(n, 1, 2, 3)
