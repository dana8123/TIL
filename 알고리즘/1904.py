import sys
sys.setrecursionlimit(1000000)

memo = {
    1: 1,
    2: 2,
}


def tile(n, memo):
    if n in memo:
        return memo[n]
    else:
        memo[n] = tile(n-1, memo) + tile(n-2, memo) % 15746
        return memo[n]


n = int(input())
print(tile(n, memo))
