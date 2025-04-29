# Key Terms
# Algorithm: A step-by-step procedure for calculations.
# Algorithmic Thinking: The ability to define clear steps to solve a problem.
# Problem Decomposition: Breaking down a complex problem into smaller, manageable parts.
# Time Complexity: A measure of the time an algorithm takes to complete as a function of the length of the input.
# Space Complexity: A measure of the amount of working storage an algorithm needs.
# Big O Notation: A mathematical notation to describe the upper limit of an algorithm's time or space complexity.
# Iteration: The repetition of a process in a computer program, often used in loops.
# Recursion: A method of solving a problem where the solution depends on solutions to smaller instances of the same problem.
# Brute Force: A straightforward approach to solving a problem, typically involving checking all possible solutions.
# Optimization: The process of making a system or design as effective or functional as possible.
# Greedy Algorithm: An algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most immediate benefit.
# Divide and Conquer: An algorithm design paradigm that works by recursively breaking down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly.
# Dynamic Programming: A method for solving complex problems by breaking them down into simpler subproblems, storing the results of subproblems to avoid redundant work.
# Backtracking: An algorithmic technique for solving problems incrementally, one piece at a time, and removing those solutions that fail to satisfy the constraints of the problem at any point of time.
#Pseudocode: A method of designing algorithms using a structured but plain language that resembles programming languages, but is intended for human reading rather than machine reading.
# Flowchart: A diagram that represents a process or algorithm, showing the steps as boxes of various kinds and their order by connecting them with arrows.
# Control Flow: The order in which individual statements, instructions, or function calls are executed or evaluated in a program.
# Data Structure: A particular way of organizing and storing data in a computer so that it can be accessed and modified efficiently.

# The Problem Solving Process:

# 1. Understand the problem: Read the problem statement carefully and make sure you understand what is being asked.

# 2. Plan the solution: Break down the problem into smaller parts and think about how to solve each part. This may involve writing pseudocode or drawing a flowchart.

# 3. Implement the solution: Write the code to solve the problem, following your plan.

# 4. Test the solution: Run your code with different test cases to make sure it works as expected. Debug any issues that arise.

# 5. Optimize the solution: If necessary, improve the efficiency of your code by reducing its time or space complexity.

# 6. Document the solution: Write comments in your code to explain what it does and how it works. This will help others (and yourself) understand your code in the future.

# 7. Reflect on the process: After solving the problem, think about what you learned and how you can apply it to future problems.

# 8. Practice: The more problems you solve, the better you will become at problem solving. Practice regularly to improve your skills.

#9. Seek help when needed: If you're stuck on a problem, don't hesitate to ask for help from peers, mentors, or online communities. Collaboration can lead to new insights and solutions.

#10. Stay updated: The field of computer science is constantly evolving. Keep learning about new algorithms, data structures, and problem-solving techniques to stay current and improve your skills.

# Common Big O Complexities:
# O(1): Constant time - The algorithm takes the same amount of time regardless of the input size.
# O(log n): Logarithmic time - The algorithm's time increases logarithmically as the input size increases.
# O(n): Linear time - The algorithm's time increases linearly with the input size.
# O(n log n): Linearithmic time - The algorithm's time increases in a linearithmic manner with the input size.
# O(n^2): Quadratic time - The algorithm's time increases quadratically with the input size.
# O(2^n): Exponential time - The algorithm's time doubles with each additional input size.
# O(n!): Factorial time - The algorithm's time increases factorially with the input size.
# This is the slowest time complexity and is often impractical for large inputs.

# Example of O(n log n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

