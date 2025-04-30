# Key Terms
# Algorithm: A step-by-step procedure for solving a problem or accomplishing a task
# Algorithmic Thinking: The process of approaching problems systematically by breaking them down and developing step-by-step solutions
# Problem Decomposition: Breaking a complex problem into smaller, more manageable subproblems
# Time Complexity: A measure of how an algorithm's runtime increases as the input size grows
# Space Complexity: A measure of how much memory an algorithm requires as the input size grows
# Big O Notation: A mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity
# Iteration: Repeating a process to generate a sequence of outcomes
# Recursion: A method where the solution depends on solutions to smaller instances of the same problem
# Brute Force: Solving a problem by trying all possible solutions
# Optimization: The process of modifying an algorithm to improve its efficiency or performance












# Pseudo-code for making a peanut butter and jelly sandwich:
# 1. Get two slices of bread
# 2. Spread peanut butter on one slice
# 3. Spread jelly on the other slice
# 4. Put the slices together with the peanut butter and jelly facing inward
# 5. Cut the sandwich in half (optional)
# 6. Serve














# The Problem-Solving Process:

# Understand the Problem
    # What are the inputs?
    # What are the expected outputs?
    # What constraints are in place?
    # Can you restate the problem in your own words?
# Devise a Plan
    # Break the problem into smaller subproblems
    # Consider known algorithms that might apply
    # Think about similar problems you've solved before
    # Start with a simple approach, even if inefficient
# Implement the Solution
    # Translate your plan into code
    # Start with pseudocode if helpful
    # Write clearly and follow your plan
# Test and Debug
    # Test with simple cases first
    # Try edge cases and larger inputs
    # Identify and fix any issues
# Optimize (if needed)
    # Look for ways to improve efficiency
    # Simplify your approach if possible
    # Consider alternative algorithms








#  Finding the maximum value in a list of numbers.

# Example Problem: Finding the Maximum Value

# Understand the Problem
    # Input: A list of numbers
    # Output: The largest number in the list
    # Constraint: The list has at least one number
# Devise a Plan
    # Initialize a variable to track the maximum value
    # Check each number in the list
    # If a number is larger than our current maximum, update the maximum
    # After checking all numbers, return the maximum
# Implement the Solution (Pseudocode)
    # function findMaximum(numbers):
    #     max = numbers[0]
    #     for each number in numbers:
    #         if number > max:
    #             max = number
    #     return max


# Test and Debug
    # Test with [1, 3, 5, 2, 4] → Expected output: 5
    # Test with [-10, -5, -7] → Expected output: -5
    # Test with [42] → Expected output: 42
# Optimize
    # This simple linear scan is already optimal for finding a maximum (O(n) time complexity)



# def find_maximum(numbers):
#     max_value = numbers[0]
#     for number in numbers:
#         if number > max_value:
#             max_value = number
#     return max_value

# print(find_maximum([1, 3, 5, 2, 4]))
# print(find_maximum([-10, -5, -7]))
# print(find_maximum([42]))





# Python Implementation:
# def find_maximum(numbers):
#     max_value = numbers[0]
#     for number in numbers:
#         if number > max_value:
#             max_value = number
#     return max_value

# # Test cases
# print(find_maximum([1, 3, 5, 2, 4]))  # 5
# print(find_maximum([-10, -5, -7]))    # -5
# print(find_maximum([42]))             # 42




















# Measuring Algorithm Efficiency:

# Execution Time: Measuring actual time taken
    # Simple but dependent on hardware, implementation, and input data
    # Useful for practical comparisons
# Operation Counting: Counting fundamental operations
    # More abstract but gives clearer insight into algorithm behavior
    # Helps identify bottlenecks
# Asymptotic Analysis: Analyzing growth patterns
    # Focuses on how algorithms scale with input size
    # Uses notations like Big O, Big Omega, and Big Theta












# Introduction to Big O Notation:

# Common Big O Complexities:
# O(1) - Constant Time
    # Runtime doesn't depend on input size
    # Example: Accessing an array element by index
# O(log n) - Logarithmic Time - Telephone book - Cutting a list in half, then cutting again and repeating until you find 
# what you were looking for
    # Runtime grows logarithmically with input size
    # Example: Binary search in a sorted array
# O(n) - Linear Time - like looking at items one by one until you find what you're looking for
    # Runtime grows linearly with input size
    # Example: Scanning through an array once
# O(n log n) - Linearithmic Time - Involves splitting and sorting -  log n splits and merging takes n time to complete
    # Often seen in efficient sorting algorithms
    # Examples: Merge sort, quick sort (average case)
# O(n²) - Quadratic Time - Ex. comparing every possible combination of 2 items. Time or steps grow proportionally to n * n. 
# If you double input size, the work grows 4 times bigger
    # Runtime grows with the square of the input size
    # Examples: Simple nested loops, bubble sort
    # [5, 3, 8, 4, 2]
    # [3, 5, 4, 2, 8]
    # [3, 4, 2, 5, 8]

# O(2^n) - Exponential Time - Number of steps double for each input
    # Runtime doubles with each additional input element - okay for small inputs, but quickly gets out of hand
    # Example: Recursive calculation of Fibonacci numbers without memoization
# O(n!) - Factorial Time - ex 3! = 3 × 2 × 1 = 6
                        #  ex 4! = 4 × 3 × 2 × 1 = 24
    # Extremely slow growth rate
    # Example: Brute force solution to traveling salesman problem
    # A, B, C, D
    #A → B → C → D → A

    # A → B → D → C → A

    # A → C → B → D → A

    # A → C → D → B → A

    # A → D → B → C → A

    # A → D → C → B → A





# # Example of O(n)
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     # return -1
#     raise ValueError(f"Target {target} not found in the array.")
# arr = [5, 8, 2, 9]
# print(linear_search(arr, 2))  # Output: 2
# print(linear_search(arr, 7))  # Output: -1

# import time
# start_time = time.time()


# Example of O(log n)
# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1

# # # 1) low = 0, high = 5 - return [2]
# # # 2) low = 3, high = 5 - return [4]
# # # 3) low = 3, high = 3 - return [3]

# arr = [1, 3, 5, 7, 9, 11]
# print(binary_search(arr, 7))  # Output: 3
# # print(binary_search(arr, 8))  # Output: -1
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Elapsed time: {elapsed_time} seconds")


# Example of O(n log n)
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left_half = merge_sort(arr[:mid])
#     right_half = merge_sort(arr[mid:])

#     return merge(left_half, right_half)

# def merge(left, right):
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result

# arr = [38, 27, 43, 3, 9, 82, 10]
# sorted_arr = merge_sort(arr)
# print(sorted_arr)

# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Elapsed time: {elapsed_time} seconds")




# Example of O(n^2)
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 # Swap
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

# arr = [5, 1, 4, 2, 8]
# bubble_sort(arr)
# print(arr)  # Output: [1, 2, 4, 5, 8]








# Space Complexity:

# O(1) - Constant Space
    # Memory usage doesn't depend on input size
    # Example: Finding the maximum value in an array (just one variable needed)
# O(n) - Linear Space
    # Memory usage grows linearly with input size
    # Example: Creating a new array with the same size as the input
# O(n²) - Quadratic Space
    # Memory usage grows with the square of the input size
    # Example: Creating a 2D matrix based on input size