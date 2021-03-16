a = input()
b = input()
a = int(a)

bnum = list(b)
print(bnum)
bnum.reverse()
for i in bnum:
    newB = int(i)
    result = newB * a
    print(result)
b = int(b)
print(a*b)
