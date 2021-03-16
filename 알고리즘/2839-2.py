sugar = int(input())

sugar_box = 0
while sugar >= 0:
    if sugar % 5 == 0:  # 5로 나누어 떨어지면,
        sugar_box += sugar // 5
        print(sugar_box)
        break
    sugar -= 3
    sugar_box += 1
else:
    print(-1)
