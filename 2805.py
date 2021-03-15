M, N = map(int, input().split())  # M = 필요한 나무길이 N = 나무의 수
tree = list(map(int, input().split()))


def gettree(Height):
    trees = 0
    for i in tree:
        if i - Height > 0:
            trees += (i - Height)
    return trees


start = 0  # (톱의 높이 h)
end = max(tree)
while (start <= end):
    mid = start + end // 2
    trees = gettree(mid)
    if trees == M:
        H = mid
    elif trees < M:
        start = mid
        H = mid

    else:
        end = mid - 1
        H = mid
    if M == trees
    break
