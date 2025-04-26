# getting the average of the class Student:

class Student:
    """A class to represent a student and their academic performance."""
     
    def __init__(self, name, scores):
        """
        Initialize a student with their name and scores.
        
        Args:
            name (str): Student's name
            scores (list): List of student's scores
            
        Raises:
            ValueError: If scores list is empty
            TypeError: If scores contains non-numeric values
        """
        self.name = name
        if not scores:
            raise ValueError("Scores list cannot be empty")
        if not all(isinstance(score, (int, float)) for score in scores):
            raise TypeError("All scores must be numeric values")
        self.scores = scores
        
    def calculate_average(self):
        """
        Calculate and return the average of student's scores.
        
        Returns:
            float: The average score rounded to 2 decimal places
        """
        if not self.scores:
            raise ValueError("No scores available to calculate average")
        return round(sum(self.scores) / len(self.scores), 2)
        
    def get_letter_grade(self):
        """
        Convert numeric average to letter grade.
        
        Returns:
            str: Letter grade (A, B, C, D, or F)
        """
        average = self.calculate_average()
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
            
    def display_report(self):
        """Display a formatted report of the student's grades."""
        average = self.calculate_average()
        grade = self.get_letter_grade()
        print(f"\nStudent Report for {self.name}")
        print("-" * 30)
        print(f"Scores: {', '.join(map(str, self.scores))}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")
