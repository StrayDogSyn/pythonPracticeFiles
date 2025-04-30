"""
Test cases for sorting algorithm benchmarks.

This module provides a collection of test cases with different characteristics
to evaluate the performance of various sorting algorithms.
"""
import random
import numpy as np

# Generate reproducible random arrays
random.seed(42)
np.random.seed(42)

def create_almost_sorted(size, swaps):
    """
    Create an almost sorted array by starting with a sorted array
    and performing a small number of random swaps.
    
    Args:
        size (int): Size of the array
        swaps (int): Number of swaps to perform
    
    Returns:
        list: Almost sorted array
    """
    arr = list(range(size))
    for _ in range(swaps):
        i, j = random.sample(range(size), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

# Dictionary of test cases
test_cases = {
    # Basic test cases
    "sorted_small": list(range(100)),
    "reversed_small": list(range(100, 0, -1)),
    "random_small": random.sample(range(1000), 100),
    
    # Medium-sized test cases
    "sorted_medium": list(range(1000)),
    "reversed_medium": list(range(1000, 0, -1)),
    "random_medium": random.sample(range(10000), 1000),
    
    # Special cases
    "duplicates": [random.randint(1, 10) for _ in range(200)],  # Many duplicate values
    "almost_sorted": create_almost_sorted(500, 10),  # Almost sorted array
    "few_unique": [random.randint(1, 5) for _ in range(200)],  # Few unique values
    
    # Edge cases
    "empty": [],
    "single": [42],
    "identical": [7] * 100,  # All elements identical
}

# Additional function to generate test arrays on demand
def generate_test_array(size, array_type="random"):
    """
    Generate a test array of the specified size and type.
    
    Args:
        size (int): Size of the array
        array_type (str): Type of array to generate. Options are:
            - "random": Random integers
            - "sorted": Pre-sorted array
            - "reversed": Reversed sorted array
            - "almost_sorted": Almost sorted array
            - "duplicates": Array with many duplicate values
    
    Returns:
        list: Generated array
    """
    if array_type == "random":
        return random.sample(range(size * 10), size)
    elif array_type == "sorted":
        return list(range(size))
    elif array_type == "reversed":
        return list(range(size, 0, -1))
    elif array_type == "almost_sorted":
        return create_almost_sorted(size, int(size * 0.05))
    elif array_type == "duplicates":
        return [random.randint(1, size // 10) for _ in range(size)]
    else:
        raise ValueError(f"Unknown array type: {array_type}")

# Validation function to check if an array is properly sorted
def is_sorted(arr, descending=False):
    """
    Check if an array is properly sorted.
    
    Args:
        arr (list): Array to check
        descending (bool): If True, check for descending order
    
    Returns:
        bool: True if the array is sorted, False otherwise
    """
    if len(arr) <= 1:
        return True
        
    for i in range(len(arr) - 1):
        if descending:
            if arr[i] < arr[i+1]:
                return False
        else:
            if arr[i] > arr[i+1]:
                return False
    return True

# Sample usage of test cases
if __name__ == "__main__":
    for name, arr in test_cases.items():
        print(f"{name}: {arr[:5]}{'...' if len(arr) > 5 else ''} (length: {len(arr)})")
        
    # Example of generating a custom test array
    custom_arr = generate_test_array(50, "almost_sorted")
    print(f"Custom almost sorted array: {custom_arr[:10]}...")