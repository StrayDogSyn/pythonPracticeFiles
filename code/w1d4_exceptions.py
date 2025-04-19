#!/usr/bin/env python3
"""
Week 1 Day 4: Python Exception Handling

This script demonstrates Python's exception handling mechanisms, showcasing how to:
1. Handle different types of exceptions
2. Use try-except-else-finally blocks
3. Raise custom exceptions
4. Create input validation with error handling
5. Implement robust error recovery

Exception handling is a critical skill for writing reliable Python code.
"""

print("=" * 60)
print("PYTHON EXCEPTION HANDLING DEMONSTRATION")
print("=" * 60)

# SECTION 1: Basic Exception Types
print("\n1. COMMON EXCEPTION TYPES")
print("-" * 60)

# Demonstrating different types of exceptions
def demonstrate_exceptions():
    """Show examples of common Python exceptions."""
    
    print("\nA. SyntaxError example (commented out to allow script to run):")
    print("   # def syntax_error():")
    print("   #     print('This function has a syntax error'")
    print("   # Missing closing parenthesis causes SyntaxError")
    
    print("\nB. IndexError example:")
    try:
        print("   Attempting to access index 5 in a list of 3 items...")
        my_list = [1, 2, 3]
        print(f"   List contents: {my_list}")
        print(f"   Accessing my_list[5]: {my_list[5]}")
    except IndexError as e:
        print(f"   ERROR CAUGHT! IndexError: {e}")
        print("   This happens when trying to access an index beyond the list bounds")
    
    print("\nC. TypeError example:")
    try:
        print("   Attempting to concatenate string and integer...")
        result = "The answer is: " + 42
        print(f"   Result: {result}")
    except TypeError as e:
        print(f"   ERROR CAUGHT! TypeError: {e}")
        print("   Fix: Convert the integer to string first with str()")
        result = "The answer is: " + str(42)
        print(f"   Correct result: {result}")
    
    print("\nD. ZeroDivisionError example:")
    try:
        print("   Attempting division by zero...")
        result = 10 / 0
        print(f"   Result: {result}")
    except ZeroDivisionError as e:
        print(f"   ERROR CAUGHT! ZeroDivisionError: {e}")
        print("   This happens when dividing any number by zero")
    
    print("\nE. KeyError example:")
    try:
        print("   Attempting to access a non-existent dictionary key...")
        my_dict = {"name": "Python", "type": "language"}
        print(f"   Dictionary contents: {my_dict}")
        print(f"   Accessing my_dict['version']: {my_dict['version']}")
    except KeyError as e:
        print(f"   ERROR CAUGHT! KeyError: {e}")
        print("   This happens when a dictionary key doesn't exist")

# Call the function to demonstrate exceptions
demonstrate_exceptions()

# SECTION 2: Try-Except-Else-Finally Pattern
print("\n2. TRY-EXCEPT-ELSE-FINALLY PATTERN")
print("-" * 60)

print("\nDemonstrating the complete try-except-else-finally structure:")
def demo_try_except_structure():
    try:
        print("1. TRY BLOCK: Code that might raise an exception")
        user_input = "10"  # Simulating user input
        value = int(user_input)
        print(f"   Converted '{user_input}' to integer: {value}")
        
        # This next line would cause an exception
        # Uncomment to see the exception handling in action
        # result = value / 0
        result = value / 2  # Safe operation
        print(f"   Calculated result: {result}")
        
    except ValueError as e:
        # Executes when a ValueError occurs
        print(f"2. EXCEPT BLOCK (ValueError): {e}")
        print("   This block handles value conversion errors")
    
    except ZeroDivisionError as e:
        # Executes when a ZeroDivisionError occurs
        print(f"2. EXCEPT BLOCK (ZeroDivisionError): {e}")
        print("   This block handles division by zero")
    
    except Exception as e:
        # Catches any other exception not specifically handled above
        print(f"2. EXCEPT BLOCK (General): An unexpected error occurred: {e}")
    
    else:
        # Executes if the try block completes with NO exceptions
        print("3. ELSE BLOCK: Executes only if no exceptions occurred")
        print("   Use this block for code that should run only if try succeeds")
    
    finally:
        # Always executes, regardless of whether an exception occurred
        print("4. FINALLY BLOCK: Always executes, no matter what")
        print("   Use for cleanup code like closing files or connections")
        
# Call the function to demonstrate the pattern
demo_try_except_structure()

# SECTION 3: Inventory Check Example
print("\n3. PRACTICAL EXAMPLE: INVENTORY CHECKER")
print("-" * 60)

# Setup inventory and orders
inventory = ['apple', 'banana', 'orange', 'grape', 'kiwi']
valid_order = ['apple', 'orange']
invalid_order = ['apple', 'pineapple']  # pineapple is not in inventory

print(f"Current inventory: {inventory}")
print(f"Valid order: {valid_order}")
print(f"Invalid order: {invalid_order}")

def check_order(order, inventory):
    """
    Check if all items in an order are available in inventory.
    
    Args:
        order (list): List of items ordered
        inventory (list): List of items in stock
        
    Returns:
        bool: True if all items are available, False otherwise
    """
    print(f"\nChecking order: {order}")
    
    if not order:  # Check for empty order
        print("WARNING: Order is empty!")
        return False
    
    for item in order:
        print(f"  Checking if '{item}' is in inventory...", end=" ")
        
        if item not in inventory:
            print("NOT FOUND!")
            print(f"  Item '{item}' is not available in inventory")
            return False
        
        print("AVAILABLE")
    
    print("All items in order are available!")
    return True

# Test with valid order
print("\nTesting with valid order:")
result = check_order(valid_order, inventory)
print(f"Order check result: {result}")

# Test with invalid order
print("\nTesting with invalid order:")
result = check_order(invalid_order, inventory)
print(f"Order check result: {result}")

# SECTION 4: Input Validation Example
print("\n4. ROBUST USER INPUT HANDLING")
print("-" * 60)

def divide_inputs(input1, input2):
    """
    Divides two numeric inputs with comprehensive error handling.

    Args:
        input1 (str): The string representation of the numerator
        input2 (str): The string representation of the denominator

    Returns:
        float: The result of the division if successful
        
    Raises:
        ValueError: If inputs cannot be converted to float or denominator is zero
        TypeError: If the inputs are not strings
    """
    print(f"Attempting to divide {input1} by {input2}")
    
    try:
        # Convert inputs to float
        print(f"  Converting {input1} to float...", end=" ")
        num1 = float(input1)
        print(f"SUCCESS: {num1}")
        
        print(f"  Converting {input2} to float...", end=" ")
        num2 = float(input2)
        print(f"SUCCESS: {num2}")
        
        # Check for zero division
        print(f"  Checking if denominator is zero...", end=" ")
        if num2 == 0:
            print("ERROR!")
            raise ValueError("Division by zero is not allowed.")
        print("SAFE")
        
        # Perform division
        print(f"  Calculating {num1} / {num2}...", end=" ")
        result = num1 / num2
        print(f"SUCCESS: {result}")
        
        return result
        
    except ValueError as e:
        if "zero" in str(e):
            print(f"  ERROR: {e}")
            print("  Hint: The denominator cannot be zero.")
        else:
            print(f"  ERROR: {e}")
            print("  Hint: Both inputs must be valid numbers.")
        raise
        
    except TypeError as e:
        print(f"  ERROR: {e}")
        print("  Hint: Both inputs must be strings that represent numbers.")
        raise

# Interactive function to get user input and handle exceptions
def get_inputs():
    """Demonstrates robust user input handling with exception management."""
    print("\nDivision Calculator with Exception Handling")
    
    try:
        # In this example, we'll simulate user input instead of actually requesting it
        # This makes the demo self-contained
        print("\nScenario 1: Valid inputs")
        input1 = "10.5"  # Simulated first user input
        input2 = "2"     # Simulated second user input
        print(f"User entered: {input1} and {input2}")
        
        result = divide_inputs(input1, input2)
        print(f"Division result: {result}")
        
        print("\nScenario 2: Division by zero")
        input1 = "8"     # Simulated first user input
        input2 = "0"     # Simulated second user input
        print(f"User entered: {input1} and {input2}")
        
        result = divide_inputs(input1, input2)
        print(f"Division result: {result}")
        
    except ValueError as e:
        print(f"Input error: {e}")
    except TypeError as e:
        print(f"Type error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("\nCalculation attempt completed.")

# Run the demo
get_inputs()

# Summary
print("\n" + "=" * 60)
print("EXCEPTION HANDLING DEMONSTRATION COMPLETE")
print("=" * 60)
print("\nKey takeaways:")
print("1. Always use try-except blocks around code that might fail")
print("2. Catch specific exceptions before general ones")
print("3. The 'else' block runs if no exceptions occur")
print("4. The 'finally' block always runs, use it for cleanup")
print("5. Raising exceptions helps signal problems properly")
print("6. Proper exception handling makes your code more robust")

