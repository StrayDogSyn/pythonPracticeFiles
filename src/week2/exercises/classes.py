# Class Methods - W2D3
# In this notebook, we will explore the concept of class methods in Python.
 
class Student:
    school_name = "JTC Python Academy"  # Class variable
    student_count = 0  # Class variable to keep track of the number of students
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
        Student.student_count += 1
        
    # add a class method to get the school name
    def display_info(self):
        print(f"Name: {self.name}, Grade: {self.grade}, School: {Student.school_name}")
# Add some students
student1 = Student("Alice", 94)
student2 = Student("Bob", 88)
student3 = Student("Charlie", 92)
student4 = Student("David", 85)

# Display student information
student1.display_info()

 # show the number of students
print(f"Total number of students: {Student.student_count}")       
        
