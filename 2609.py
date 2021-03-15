num1, num2 = map(int, input().split())
a, b = num1, num2

while b != 0:
    a = a % b
    a, b = b, a

print(a)
print(num1*num2 // a)
