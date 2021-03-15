import sys
numbers = int(input())
new_list = []


for i in range(numbers):
    new_list.append(int(sys.stdin.readline()))
for i in sorted(new_list):
    sys.stdout.write(str(i)+'\n')
