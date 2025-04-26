def add(a, b):
    """Return the sum of a and b."""
    return a + b
def subtract(a, b):
    """Return the difference of a and b."""
    return a - b
def multiply(a, b):
    """Return the product of a and b."""
    return a * b
def divide(a, b):
    """Return the quotient of a and b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def power(a, b):
    """Return a raised to the power of b."""
    return a ** b
def square_root(a):
    """Return the square root of a."""
    if a < 0:
        raise ValueError("Cannot take square root of negative number.")
    return a ** 0.5
def factorial(n):
    """Return the factorial of n."""
    if n < 0:
        raise ValueError("Cannot take factorial of negative number.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n < 0:
        raise ValueError("Cannot take Fibonacci of negative number.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
def gcd(a, b):
    """Return the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a
