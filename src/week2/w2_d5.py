def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32

def display_temperature(location, temp_c):
    """
    Display temperature conversion for a given location.
    
    Args:
        location (str): Description of the temperature location
        temp_c (float): Temperature in Celsius
    """
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"{location}: {temp_c}°C is {temp_f:.1f}°F")

# Temperature conversions for different scenarios
temperatures = {
    "Room temperature": 22,
    "Outdoor temperature": 15,
    "Body temperature": 37
}

# Display all temperature conversions
for location, temp_c in temperatures.items():
    display_temperature(location, temp_c)

### Refactoring ###

class Student:
    def __init__(self, name, scores):
        """
        Initialize a student with their name and scores.
        
        Args:
            name (str): Student's name
            scores (list): List of student's scores
        """
        self.name = name
        self.scores = scores
        
    def calculate_average(self):
        """Calculate and return the average of student's scores."""
        return sum(self.scores) / len(self.scores)
    
    def get_letter_grade(self, average):
        """
        Convert numeric average to letter grade.
        
        Args:
            average (float): Student's average score
            
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
    
    def display_report(self):
        """Display a formatted report of the student's grades."""
        average = self.calculate_average()
        grade = self.get_letter_grade(average)
        print(f"\nStudent: {self.name}")
        print(f"Scores: {', '.join(map(str, self.scores))}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")

def main():
    """Main function to run the Student Grade Calculator."""
    print("Welcome to the Student Grade Calculator")
    
    # Student data
    students = [
        Student("Alex", [85, 90, 78]),
        Student("Taylor", [92, 88, 95]),
        Student("Jordan", [76, 82, 79])
    ]
    
    # Process and display each student's grades
    for student in students:
        student.display_report()
    
    print("\nThank you for using the Student Grade Calculator!")

if __name__ == "__main__":
    main()