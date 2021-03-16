max = 21

memo = [[[0 for col in range(max)] for row in range(max)]
        for depth in range(max)]
# [[[0,0,0,...0][0,0,0,...0][0,0,0,...0]...[0,0,0,...0(21개)](21개)](21개)]


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if memo[a][b][c]:
        print(f'memo[{a}][{b}][{c}] = {memo{a}{b}{c}}')
        return memo[a][b][c]

    if a < b < c:
        print()
