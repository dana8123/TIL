case = int(input())
for i in range(case):
    room = 0
    rooms = []
    data = list(map(int, input().split()))
    H = int(data[0])
    W = int(data[1])
    N = int(data[2])
    for i in range(0, W):
        room = room + 1           # room = 1
        for i in range(1, H+1):
            floor = room + (i * 100)   # room = 1
            rooms.append(floor)
    print(rooms[N-1])
[101, 102, 103.....]
[101, 201, 301....]
