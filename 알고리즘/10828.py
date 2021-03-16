case = int(input())
stack = []
for i in range(case):
    command = list(input().split())
    if "push" in command:
        stack.append(command[1])
        print(stack[-1])
    # 스택~에서 가장 위에 있는 정수를 고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif "pop" in command:  # 에러 발생, stack에 값이 있다가 없어지면? pop할 때 에러남..
        if stack:
            stack.remove(stack[0])

        if not stack:
            print(-1)
    # 스택에 들어있는 정수의 개수를 출력한다.
    elif "size" in command:
        print(len(stack))
    elif "empty" in command:
        if not stack:
            print(1)
        if stack:
            print(0)
    # 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif "top" in command:
        if not stack:
            print('-1')
        if stack:
            print(stack[0])  # 이거 왜 프린트되지..?
