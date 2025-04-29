def bubble_sort(arr):
    length = len(arr)
    
    for pass_num in range(length):
        for j in range(0, length-pass_num-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Unsorted array: {arr}")

sorted_arr = bubble_sort(arr)
print(f"Sorted array: {sorted_arr}")
