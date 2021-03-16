sval = input().upper()
word = list(sval)
wset = list(set(word))
cntlist = []

for i in wset:
    cnt = word.count(i)  # wset에 들어있는 인자별로 개수를 세줌
    cntlist.append(cnt)
if (cntlist.count(max(cntlist)) >= 2):
    print('?')
else:
    print(wset[cntlist.index(max(cntlist))])
