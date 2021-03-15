case = int(input())
count = 0
for i in range(case):
    word = input()
    alphabet = []
    for j in range(len(word) - 1):  # happy
        # aaabccd의 경우, a는 전자에 속해서, b는 후자에 속해서 들어감.
        if word[j] not in alphabet and word[j] != word[j+1]:
            alphabet.append(word[j])  # 연속된 알파벳은 여기 들어갈거임.
        else:
            alphabet.clear()

    if len(alphabet) != 0:
        count = count + 1
print(count)
