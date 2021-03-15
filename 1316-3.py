N = int(input())

answer = 0

for i in range(N):
    word = input()               # len(happy) = 5
    for j in range(len(word)):   # range(5) = 0 1 2 3 4
        if j != len(word)-1:
            if word[j] == word[j+1]:
                pass
            elif word[j] in word[j+1:]:
                break
        else:
            answer += 1
print(answer)
