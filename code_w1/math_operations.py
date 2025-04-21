#!/usr/bin/env python3
"""
Basic Math Operations Module

This module provides fundamental mathematical operations that can be imported
and used in other Python scripts. Each function is designed to be simple and
illustrate basic Python function concepts.

Functions:
    add(a, b): Returns the sum of two numbers
    subtract(a, b): Returns the difference between two numbers
    multiply(a, b): Returns the product of two numbers
    divide(a, b): Returns the quotient of two numbers with zero division handling

Note: While Python's built-in math module provides similar functionality,
this module serves as an educational example of creating custom modules.
"""

def add(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a (number): The first number
        b (number): The second number
        
    Returns:
        number: The sum of a and b
    
    Example:
        >>> add(5, 3)
        8
    """
    print(f"Adding {a} and {b}")
    result = a + b
    print(f"Result of {a} + {b} = {result}")
    return result

def subtract(a, b):
    """
    Subtract b from a and return the result.
    
    Args:
        a (number): The number to subtract from
        b (number): The number to subtract
        
    Returns:
        number: The difference between a and b
    
    Example:
        >>> subtract(10, 4)
        6
    """
    print(f"Subtracting {b} from {a}")
    result = a - b
    print(f"Result of {a} - {b} = {result}")
    return result

def multiply(a, b):
    """
    Multiply two numbers and return the result.
    
    Args:
        a (number): The first number
        b (number): The second number
        
    Returns:
        number: The product of a and b
    
    Example:
        >>> multiply(4, 5)
        20
    """
    print(f"Multiplying {a} and {b}")
    result = a * b
    print(f"Result of {a} * {b} = {result}")
    return result

def divide(a, b):
    """
    Divide a by b and return the result.
    Handles division by zero by returning an error message.
    
    Args:
        a (number): The dividend
        b (number): The divisor
        
    Returns:
        number or str: The quotient of a and b, or an error message if b is 0
    
    Example:
        >>> divide(20, 5)
        4.0
        >>> divide(10, 0)
        'Cannot divide by zero'
    """
    print(f"Dividing {a} by {b}")
    
    # Check for division by zero
    if b == 0:
        print("ERROR: Cannot divide by zero!")
        return "Cannot divide by zero"
    
    result = a / b
    print(f"Result of {a} / {b} = {result}")
    return result

# If this module is run directly (not imported), run some tests
if __name__ == "__main__":
    print("\nRunning tests of the math_operations module:")
    print("-------------------------------------------")
    
    # Test addition
    print("\nTesting addition:")
    assert add(5, 3) == 8, "Addition test failed"
    assert add(-1, 1) == 0, "Addition test with negative number failed"
    
    # Test subtraction
    print("\nTesting subtraction:")
    assert subtract(10, 5) == 5, "Subtraction test failed"
    assert subtract(5, 10) == -5, "Subtraction test resulting in negative failed"
    
    # Test multiplication
    print("\nTesting multiplication:")
    assert multiply(4, 5) == 20, "Multiplication test failed"
    assert multiply(-2, 3) == -6, "Multiplication test with negative number failed"
    
    # Test division
    print("\nTesting division:")
    assert divide(20, 5) == 4.0, "Division test failed"
    assert divide(5, 2) == 2.5, "Division test with decimal result failed"
    assert divide(10, 0) == "Cannot divide by zero", "Division by zero test failed"
    
    print("\nAll tests passed! The math_operations module is working correctly.")