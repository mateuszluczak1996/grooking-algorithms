# Check if element is in list using binary search
def is_in_list(item, numbers):
    sortedNumbers = sorted(numbers)

    start = 0
    end = len(sortedNumbers) - 1

    comparisions = 0

    while start <= end:

        middle = (start + end) // 2
        guess = sortedNumbers[middle]

        if guess < item:
            start = middle + 1
        elif guess > item:
            end = middle - 1
        else:
            print(f"Number of comparisions: {comparisions}")
            return True

        comparisions = comparisions + 1

    print(f"Number of comparisions: {comparisions}")
    return False


list = [1, 8, 2, 5, 3, 4, 9, 12, 13, 20, 23, 21, 30, 32]

print(is_in_list(11, list))
print(is_in_list(8, list))
