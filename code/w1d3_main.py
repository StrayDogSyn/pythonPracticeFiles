# In a new file named import_demo.py:

# Importing the custom module 'math_operations' which contains mathematical functions like add and multiply.
import math_operations
# Importing the 'sys' module to access system-specific parameters and functions, such as the module search path.
import sys
import os
import math
import random
import time
# these are all libraries that are used in the code

# Using the 'add' function from 'math_operations' to calculate the sum of 5 and 3.
result = math_operations.add(5, 3)
# Printing the result of the addition operation.
print(f"5 + 3 = {result}")

# Using the 'multiply' function from 'math_operations' to calculate the product of 4 and 6.
result = math_operations.multiply(4, 6)
# Printing the result of the multiplication operation.
print(f"4 * 6 = {result}")

# Iterating through the system's module search paths to display where Python looks for modules.
for path in sys.path:
    # Printing each path in the module search path list.
    print(f' - {path}')
