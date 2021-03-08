num = inp = int(input())
count = 0
while True:
    ten = num // 10
    one = num % 10
    result = ten + one
    count += 1
    num = int(str(num % 10) + str(result % 10))
    if(num == inp):
        break
print(count)
