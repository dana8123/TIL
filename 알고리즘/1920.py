# 두 리스트를 비교하기 위해 sort시켜줌.
# B의 중간값과 A의 끝값을 비교하여 B > A라면, 왼쪽항을 B < A라면 오른쪽값을 탐색한다.
# 왼쪽항은 start~mid까지, 오른쪽항은 mid+1~end까지 탐색한다.
# 같은값 발견 시 true를 뱉어
# 탐색하면서 또다시 중간값과 비교하면서 위의 행동을 반복한다.
# 반복문의 종료 조건 : 더이상 찾을 구간이 없을 때, 즉 시작값이 끝값보다 커진다면 종료다.
n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))


def binary(arr, val, start, end):
    mid = (start + end) // 2
    if start > end:
        return 0
    if arr[mid] == val:  # a의 중간값과 b의 요소들을 비교하는 방식
        return 1
    elif arr[mid] > val:  # 중간값이 더 크다면, 앞쪽에서 탐색
        return binary(arr, val, start, mid-1)
    else:  # 중간값이 작다면 뒷쪽에서 탐색
        return binary(arr, val, mid+1, end)


for val in b:
    start = 0
    end = len(a)-1
    print(binary(a, val, start, end))
