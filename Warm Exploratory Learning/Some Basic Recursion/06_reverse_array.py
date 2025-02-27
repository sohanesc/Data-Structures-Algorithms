def reverse_array(arr, start, end):
    if start >= end:
        return
    # Swap the elements at start and end
    arr[start], arr[end] = arr[end], arr[start]
    # Recursive call to reverse the remaining array
    reverse_array(arr, start + 1, end - 1)

arr = [1, 2, 3, 4, 5]
reverse_array(arr, 0, len(arr) - 1)
print(arr)
