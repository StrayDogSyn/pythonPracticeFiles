# Basic merge sort implementation
def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.
    
    Args:
        arr (list): The array to be sorted.
        
    Returns:
        list: The sorted array.
    """
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]        # Dividing the elements into 2 halves
        R = arr[mid:]

        merge_sort(L)        # Sorting the first half
        merge_sort(R)        # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

arr = [38, 27, 43, 3, 9, 82, 10]
print("Unsorted array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
