case = int(input())
num = list(map(int, input().split()))
result = 0

max_num = max(num)
min_num = min(num)

result = max_num * min_num

print(result)
