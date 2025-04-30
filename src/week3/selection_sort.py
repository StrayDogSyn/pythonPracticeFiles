# Basic selection sort implementation
def selection_sort(arr):
    """
    Sorts an array using the selection sort algorithm.
    
    Args:
        arr (list): The array to be sorted.
        
    Returns:
        list: The sorted array.
    """
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

arr = [64, 25, 12, 22, 11]
print("Unsorted array:", arr)
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
