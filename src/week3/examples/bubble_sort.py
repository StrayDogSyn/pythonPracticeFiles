# Basic bubble sort implementation
def bubble_sort(arr):
    """
    Sorts an array using the bubble sort algorithm.
    
    Args:
        arr (list): The array to be sorted.
        
    Returns:
        list: The sorted array.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", arr)
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
