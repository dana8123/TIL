from collections import deque

case = int(input())
card_list = deque()

for i in range(0, case):
    card_list.append(i + 1)

while len(card_list) > 1:
    card_list.popleft()   # 1 2 3 4 > 2 3 4   # 4 2
    card_list.append(card_list[0])  # 3 4 2   #
    card_list.pop()

print(card_list.pop())
