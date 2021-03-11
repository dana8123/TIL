from collections import deque

n, m = map(int, input().split())
dq = deque()
for i in range(n):
    dq = dq.append(n)
    s = input().split()
    count = 0
    for j in s:  # [1, 2, 3]
    if dq[0] == j or dq[-1] == j:
        if dq[0] == n:  # 안움직여도 되는 상황
            dp.popleft()
        elif dq[-1] == j:
            dq.pop()
    else:
        if (dq(index(j)) < len(dq) - dq(index(j))):
            # 왼쪽항이 더 가깝다는 이야기
            count += 1
            dq.append(dq[0])   1 2 3 4 5 6 > 1 2 3 4 5 6 1 > 2 3 4 5 6 1
            del dq[0]
        else:
            # 오른쪽항이 더 가깝다는 이야기
            count += 1
            dq.appendleft(dq[-1])
            dq.pop()
    print(count)
