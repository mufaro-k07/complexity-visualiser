import numpy as np

# Taking the different sorting algorithms from factorial.py

def linear_search(n):
    for i in range(n):
        if i == n - 1:
            return i


def bubble_sort(n):
    arr = np.random.randint(0, 100, n)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def binary_search(n):
    arr = sorted(np.random.randint(0, 100, n))
    target = arr[-1]
    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def nested_loops(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count
