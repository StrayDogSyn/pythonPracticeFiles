from typing import List, TypeVar, Optional, Callable, Any

# Define a more flexible TypeVar for comparable types
T = TypeVar('T')

def bubble_sort(arr: List[T], descending: bool = False, key: Optional[Callable[[T], Any]] = None) -> List[T]:
    """
    Sorts an array using the bubble sort algorithm.
    
    Args:
        arr (List[T]): List of comparable items to sort
        descending (bool): If True, sorts in descending order. Defaults to False.
        key (Optional[Callable[[T], Any]]): A function that extracts a comparison key from each element.
                                           If None, compares elements directly. Defaults to None.
    
    Returns:
        List[T]: The sorted list
        
    Raises:
        ValueError: If the input array is empty
        TypeError: If the array contains mixed non-comparable types
        
    Time Complexity:
        - Best case: O(n) when array is already sorted
        - Average case: O(n²)
        - Worst case: O(n²)
    Space Complexity:
        - O(n) due to the copy of the input array
    """
    # Validate input
    if not arr:
        raise ValueError("Cannot sort an empty array")
    
    # Create a copy to avoid modifying the original array
    result = arr.copy()
    length = len(result)
    
    # Define comparison function based on parameters
    def should_swap(i: int, j: int) -> bool:
        """Determine if elements at positions i and j should be swapped based on sort order."""
        if key:
            # Use key function if provided
            if descending:
                return key(result[i]) < key(result[j])
            return key(result[i]) > key(result[j])
        else:
            # Direct comparison
            try:
                if descending:
                    return result[i] < result[j]
                return result[i] > result[j]
            except TypeError:
                raise TypeError("Elements must be comparable to each other") from None
    
    # Perform bubble sort
    for pass_num in range(length):
        swapped = False
        # Last pass_num elements are already in place
        for j in range(length - pass_num - 1):
            if should_swap(j, j+1):
                # Swap elements
                result[j], result[j+1] = result[j+1], result[j]
                swapped = True
        
        # Early stopping optimization if no swaps were made
        if not swapped:
            break
    
    return result


def benchmark_sort(arr: List[T]) -> None:
    """
    Benchmark the bubble sort algorithm on the given array.
    
    Args:
        arr (List[T]): The array to sort and benchmark
    """
    import time
    
    start_time = time.time()
    sorted_arr = bubble_sort(arr)
    end_time = time.time()
    
    print(f"Sorting took {end_time - start_time:.6f} seconds")
    return sorted_arr


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
    
    # Example with key function
    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 20},
        {"name": "Charlie", "age": 30}
    ]
    print("\nSorting dictionary by age:")
    sorted_people = bubble_sort(people, key=lambda x: x["age"])
    for person in sorted_people:
        print(f"{person['name']}: {person['age']}")
