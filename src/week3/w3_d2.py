# Example of O(n log n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example of O(n^2)
def bubble_sort(arr):
    # Get the length of the array to determine how many passes we need
    length = len(arr)
    
    # Outer loop: each pass will place the largest unsorted element at the end
    # We need at most n passes for an array of size n
    for pass_num in range(length):
        # Inner loop: compare adjacent elements and swap if they're in the wrong order
        # With each pass, we can reduce the number of comparisons since the largest elements
        # are already in their correct positions at the end
        for j in range(0, length-pass_num-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap the elements if they are in the wrong order
                # This gradually "bubbles up" larger elements to the end of the array
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
