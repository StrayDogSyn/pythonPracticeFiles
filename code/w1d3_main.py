#!/usr/bin/env python3
"""
Python Module Import Demo

This script demonstrates how to import and use Python modules, both custom and built-in.
It shows various import techniques and module access patterns, which are fundamental
concepts in Python programming.

Topics covered:
1. Importing custom modules
2. Importing built-in modules
3. Accessing functions from imported modules
4. Understanding Python's module search path

This is typically taught during Week 1, Day 3 of Python courses.
"""

print("=" * 50)
print("PYTHON MODULE IMPORT DEMONSTRATION")
print("=" * 50)

# Import our custom math_operations module that contains basic math functions
print("\n1. Importing custom module 'math_operations'...")
import math_operations

# Import built-in system modules for various operations
print("\n2. Importing built-in modules...")
import sys      # System-specific parameters and functions
import os       # Operating system interfaces
import math     # Mathematical functions
import random   # Generate random numbers
import time     # Time access and conversions

print("All modules imported successfully!")

# Using the custom module functions
print("\n3. Using functions from our custom math_operations module:")
print("-" * 60)

# Demonstrate the add function
print("\nDemonstration of math_operations.add():")
result_add = math_operations.add(5, 3)
print(f"Result stored in variable: {result_add}")

# Demonstrate the multiply function
print("\nDemonstration of math_operations.multiply():")
result_multiply = math_operations.multiply(4, 6)
print(f"Result stored in variable: {result_multiply}")

# Demonstrate using built-in modules
print("\n4. Using functions from built-in modules:")
print("-" * 60)

# Using math module
print("\nUsing math module:")
print(f"Value of π (pi): {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")

# Using random module
print("\nUsing random module:")
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")

# Using time module
print("\nUsing time module:")
current_time = time.time()
formatted_time = time.ctime(current_time)
print(f"Current timestamp: {current_time}")
print(f"Formatted time: {formatted_time}")

# Demonstrate the module search path
print("\n5. Python's module search paths:")
print("-" * 60)
print("Python looks for modules in these locations (in order):")

# Iterate through each path in the sys.path list
for i, path in enumerate(sys.path, 1):
    print(f"  Path {i}: {path}")

# Show current working directory
print("\n6. Current working directory:")
print("-" * 60)
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Conclusion
print("\n" + "=" * 50)
print("MODULE IMPORT DEMONSTRATION COMPLETE")
print("=" * 50)
print("\nKey takeaways:")
print("1. Use 'import module_name' to import modules")
print("2. Access module functions with 'module_name.function_name()'")
print("3. Python searches for modules in the paths listed in sys.path")
print("4. Both custom and built-in modules are imported the same way")
