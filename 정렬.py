input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array)
    for i in range(n):
        index_min = i
        for j in range(n - i):
            if array[i + j] < array[index_min]:
                index_min = i + j
        array[i], array[index_min] = array[index_min], array[i]
    return


selection_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
