# Main program for student grade processing
from student_processor import Student

def main():
    """Main function to run the Student Grade Calculator."""
    print("\nWelcome to the Student Grade Calculator")
    print("=" * 40)
    
    # Student data with test scores
    students = [
        Student("Alex", [85, 90, 78, 88]),
        Student("Taylor", [92, 88, 95, 85]),
        Student("Jordan", [76, 82, 79, 84])
    ]
    
    try:
        # Process and display each student's grades
        for student in students:
            student.display_report()
        
        # Calculate and display class statistics
        class_averages = [student.calculate_average() for student in students]
        class_average = round(sum(class_averages) / len(class_averages), 2)
        
        print("\nClass Statistics")
        print("=" * 40)
        print(f"Number of students: {len(students)}")
        print(f"Class average: {class_average}")
        
    except (ValueError, TypeError) as e:
        print(f"\nError processing grades: {e}")
    except Exception as e:
        print(f"\nUnexpected error: {e}")
    
    print("\nThank you for using the Student Grade Calculator!")

if __name__ == "__main__":
    main()