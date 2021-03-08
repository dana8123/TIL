cases = int(input())
count = 0
score = []
while True:
    data = list(map(int, input().split()))
    students = data[0]
    score = data[1:]
    scores = sum(score)
    avg = scores / students
    num = 0
    for i in score:
        if i > avg:
            num += 1
    print(format((num / data[0]) * 100, ".3f") + '%')
    count += 1
    if cases == count:
        break
