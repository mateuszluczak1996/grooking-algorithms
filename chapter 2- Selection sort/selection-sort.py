
from typing import List


def find_smallest(list: List) -> int:
    smallest = list[0]
    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]
    return smallest


def selection_sort(list: List) -> List:
    result_list = []
    while list:
        smallest = find_smallest(list)
        list.remove(smallest)
        result_list.append(smallest)

    return result_list


sorted_list = selection_sort([20, 10, 5, 1, 5, 13, 34, 21, 3, 10])
print(sorted_list)

