# 21.03.16
# 백준 18258
# 백준 10828과 풀이법이 유사함.
# 다만 pop 실행 시, queue가 비었을 때, 마지막 숫자와 -1이 동시에 나오는 에러가 있었음
# 따로 분기처리(else문) 후 if not queue를 사용하니 정상작동.
from collections import deque
import sys

case = int(input())
queue = deque()
for i in range(case):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            if not queue:
                print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if queue:
            print(0)
        if not queue:
            print(1)
    elif command[0] == 'front':
        if queue:
            print(queue[0])
        if not queue:
            print(-1)
    elif command[0] == 'back':
        if queue:
            print(queue[-1])
        if not queue:
            print(-1)
