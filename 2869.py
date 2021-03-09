import math
A, B, V = map(int, input().split())

n = (V - B) / (A - B)
n = math.ceil(n)
print(n)

# math.ceil없이 쓴다면?
