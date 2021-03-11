input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    # 이 부분을 채워보세요!
    n = len(array)
    for i in range(n):
        for j in range(1, n):  # 5 - (0,1,2,3,4) - 1 = 4,3,2,1,0
            if array[j] > array[j + 1]:  # 0번째가 1번째보다 크면
                array[j], array[j + 1] = array[j+1], array[j]  # 두 배열의 순서를 바꿔라
    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
