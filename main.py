# from math import inf
# x = 0b10110111
# print(bin(x >> 3))
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return left  # Target not found

arr = [1, 3, 5, 7, 9, 11]
target = 8

index = binary_search(arr, target)
print(index)  # Output: 3
