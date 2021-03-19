import sys
sys.setrecursionlimit(1000000)

n = int(input())
memo = list()
memo[1], memo[2] = 1, 2

for i in range(3, n+1):
    memo[n] = memo(n-1) + memo(n-2) % 15746

print(memo[n])
