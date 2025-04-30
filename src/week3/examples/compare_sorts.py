import time
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from test_cases import test_cases
try:
    from tabulate import tabulate
except ImportError:
    print("tabulate package not found. Installing...")
    import subprocess
    subprocess.check_call(['pip', 'install', 'tabulate'])
    from tabulate import tabulate

def time_function(func, *args, **kwargs):
    """
    Measure the execution time of a function.
    
    Args:
        func: The function to time
        *args: Arguments to pass to the function
        **kwargs: Keyword arguments to pass to the function
        
    Returns:
        float: The time taken to execute the function in seconds
    """
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time

def main():
    # Define the sorting algorithms to compare
    algorithms = {
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Bubble Sort": bubble_sort,
    }

    # Prepare the results table
    results = []

    # Iterate through each test case
    for name, arr in test_cases.items():
        print(f"Running tests for: {name}")
        for algo_name, algo in algorithms.items():
            # Time the sorting algorithm
            time_taken = time_function(algo, arr.copy())
            results.append((name, algo_name, time_taken))

    # Print the results in a tabular format
    print(tabulate(results, headers=["Test Case", "Algorithm", "Time (seconds)"], tablefmt="grid"))

if __name__ == "__main__":
    main()