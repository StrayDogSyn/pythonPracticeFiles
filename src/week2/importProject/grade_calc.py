"""
This module provides functionality for grade calculations and reporting.
Includes functions for calculating averages, converting to letter grades,
and generating student grade reports.
"""

def validate_scores(scores):
    """
    Validate that scores are valid numeric values.
    
    Args:
        scores (list): List of scores to validate
        
    Raises:
        ValueError: If scores list is empty
        TypeError: If scores contains non-numeric values
    """
    if not scores:
        raise ValueError("Scores list cannot be empty")
    if not all(isinstance(score, (int, float)) for score in scores):
        raise TypeError("All scores must be numeric values")

def calculate_average(scores):
    """
    Calculate and return the average of scores.
    
    Args:
        scores (list): List of numeric scores
        
    Returns:
        float: The average score rounded to 2 decimal places
        
    Raises:
        ValueError: If scores list is empty
    """
    validate_scores(scores)
    return round(sum(scores) / len(scores), 2)

def get_letter_grade(average):
    """
    Convert numeric average to letter grade.
    
    Args:
        average (float): Numeric grade average
        
    Returns:
        str: Letter grade (A, B, C, D, or F)
    """
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def generate_grade_report(name, scores):
    """
    Generate a formatted report of the student's grades.
    
    Args:
        name (str): Student's name
        scores (list): List of student's scores
        
    Returns:
        str: Formatted grade report
    """
    validate_scores(scores)
    average = calculate_average(scores)
    grade = get_letter_grade(average)
    
    report = f"\nStudent Report for {name}\n"
    report += "-" * 30 + "\n"
    report += f"Scores: {', '.join(map(str, scores))}\n"
    report += f"Average: {average:.2f}\n"
    report += f"Grade: {grade}"
    return report

def display_grade_report(name, scores):
    """
    Display a formatted report of the student's grades.
    
    Args:
        name (str): Student's name
        scores (list): List of student's scores
    """
    print(generate_grade_report(name, scores))