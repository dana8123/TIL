while True:
    sval = input()
    if sval == '.':
        break
    stk = []
    temp = True
    for i in sval:
        if i == '(' or i == '[':
            stk.append(i)
        elif i == ')':
            if stk.is_empty() or stk[-1] == '[':
                temp = False
                break
            elif stk[-1] == '(':
                stk.pop()
        elif i == ']':
            if not stk or stk[-1] == '(':
                temp = False
                break
            elif stk[-1] == '[':
                stk.pop()
    if temp == True and not stk:
        print('yes')
    else:
        print('no')
