num, goal = map(int, input().split())
val = []
count = 0

for i in range(num):
    val.append(int(input()))

for i in range(1, num+1):
    coin = val[-i]
    if coin <= goal:
        result = goal // coin
        goal -= result * coin
        count += result

print(count)
