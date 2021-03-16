# 21.03.16
# 백준 10828 번 풀이
# if ~ in 을 command[0] == 해당값 으로 수정하면 좀 더 깔끔한 코드가 나올 것
import sys
case = int(input())
stack = []
for i in range(case):
    command = list(sys.stdin.readline().split())
    if "push" in command:
        stack.append(command[1])
    elif "pop" in command:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif "size" in command:
        print(len(stack))
    elif "empty" in command:
        if not stack:
            print(1)
        else:
            print(0)
    # 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif "top" in command:
        if not stack:
            print('-1')
        else:
            print(stack[-1])  # 이거 왜 프린트되지..?
