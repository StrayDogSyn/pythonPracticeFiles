# Basic insertion sort implementation
def insertion_sort(arr):
    """
    Sorts an array using the insertion sort algorithm.
    
    Args:
        arr (list): The array to be sorted.
        
    Returns:
        list: The sorted array.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

arr = [12, 11, 13, 5, 6]
print("Unsorted array:", arr)
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
