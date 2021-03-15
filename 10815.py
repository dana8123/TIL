sangun_case = int(input())
sangun_card = list(map(int, input().split()))
sangun_card.sort()
case = int(input())
card = list(map(int, input().split()))


def cardGame(sangun_card):
    for i in card:
        if 0 <= mid < end:  # 중간값이 0번째, 혹은 마지막 숫자보다 작을 때 까지만 실행
            if sangun_card[end + 1] == i:
                print(1, ' ')
            else:
                print(0, ' ')


for i in card:
    start, end = 0, sangun_case
    while start <= end:
        mid = start + end // 2
        if sangun_card[mid] < i:
            start = mid + 1
        else:  # 반대로 상근이가 갖고있는 카드가 주어진 카드의 수보다 작다면, 상근카드의 왼쪽부분을 탐색
            end = mid - 1

cardGame()
