"""
Assignment-24: Sorting
1. Write a python function to implement bubble sort
2. Write a python function to implement modified bubble sort.
"""

def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def modified_bubble_sort(arr):
    flag = False
    for i in range(1, len(arr)):
        flag = False
        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:
            break
    return arr


l = [5, 4, 3, 2, 1]
print(modified_bubble_sort(l))
