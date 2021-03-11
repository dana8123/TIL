case = int(input())
stk = []
result = []
temp = True
count = 0
for i in range(0, case):
    nums = int(input())
    while count < nums:
        count += 1
        stk.append(count)
        result.append('+')
    if stk[-1] == nums:
        stk.pop()
        result.append('-')
    else:
        temp = False


if temp == False:
    print('오..안돼!')
else:
    print("\n".join(result))
