from typing import List, TypeVar, Optional, Union

T = TypeVar('T', int, float, str)

def bubble_sort(arr: List[T], descending: bool = False) -> List[T]:
    """
    Sorts an array using the bubble sort algorithm.
    
    Args:
        arr (List[T]): List of comparable items to sort
        descending (bool): If True, sorts in descending order. Defaults to False.
    
    Returns:
        List[T]: The sorted list
        
    Raises:
        ValueError: If the input array is empty
        TypeError: If the array contains mixed types
    """
    if not arr:
        raise ValueError("Cannot sort an empty array")
    
    # Check for consistent types
    if not all(isinstance(x, type(arr[0])) for x in arr):
        raise TypeError("All elements must be of the same type")
    
    length = len(arr)
    # Create a copy to avoid modifying the original array
    result = arr.copy()
    
    for pass_num in range(length):
        swapped = False
        for j in range(0, length-pass_num-1):
            # Change comparison based on sort order
            should_swap = result[j] < result[j+1] if descending else result[j] > result[j+1]
            if should_swap:
                result[j], result[j+1] = result[j+1], result[j]
                swapped = True
        # Early stopping if no swaps were made
        if not swapped:
            break
    
    return result

# Example usage
if __name__ == "__main__":
    # Test with different types of arrays
    int_arr = [64, 34, 25, 12, 22, 11, 90]
    float_arr = [64.1, 34.2, 25.3, 12.4]
    str_arr = ["banana", "apple", "cherry", "date"]

    print("Integer array:")
    print(f"Unsorted: {int_arr}")
    print(f"Sorted ascending: {bubble_sort(int_arr)}")
    print(f"Sorted descending: {bubble_sort(int_arr, descending=True)}")
    
    print("\nFloat array:")
    print(f"Unsorted: {float_arr}")
    print(f"Sorted ascending: {bubble_sort(float_arr)}")
    
    print("\nString array:")
    print(f"Unsorted: {str_arr}")
    print(f"Sorted ascending: {bubble_sort(str_arr)}")
