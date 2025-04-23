# OOP approach using a Restaurant class
class Restaurant:
    """A class to represent a restaurant with its details."""
    
    def __init__(self, name):
        """Initialize a restaurant with a name and default values."""
        self.name = name
        self.addresses = []
        self.menu_url = ''
        self.hours = {
            'Sunday': None,
            'Monday': None,
            'Tuesday': None,
            'Wednesday': None,
            'Thursday': None,
            'Friday': None,
            'Saturday': None,
        }
    
    def update_hours(self, day, opening, closing):
        """Update the opening and closing hours for a specific day."""
        if day not in self.hours:
            raise ValueError(f"Invalid day: {day}")
        
        if not (0 <= opening <= 24) or not (0 <= closing <= 24):
            raise ValueError("Hours must be between 0 and 24")
            
        self.hours[day] = [opening, closing]
    
    def is_open(self, day, time):
        """Check if the restaurant is open at a specific time on a specific day."""
        hours_for_day = self.hours[day]
        
        # Restaurant is closed if no hours are set
        if hours_for_day is None:
            return False
            
        return hours_for_day[0] <= time < hours_for_day[1]
    
    def add_address(self, address):
        """Add a new address for the restaurant."""
        self.addresses.append(address)
    
    def set_menu_url(self, url):
        """Set the menu URL for the restaurant."""
        self.menu_url = url
    
    def __str__(self):
        """Return a string representation of the restaurant."""
        return f"{self.name} Restaurant"
    
    def display_hours(self):
        """Display formatted hours for the restaurant."""
        print(f"Hours for {self.name}:")
        for day, hours in self.hours.items():
            if hours is None:
                print(f"  {day}: Closed")
            else:
                print(f"  {day}: {hours[0]}:00 - {hours[1]}:00")

# Creating a restaurant using our class
islands = Restaurant('Islands')
spudz = Restaurant('Spudz')

# Using the methods
islands.update_hours('Wednesday', 8, 17)
islands.add_address("123 Beach Blvd, Anaheim, CA")
islands.set_menu_url("https://islands.com/menu")

# Display restaurant information
print(islands)
islands.display_hours()
print(f"Is {islands.name} open at noon on Wednesday? {islands.is_open('Wednesday', 12)}")
print(f"Is {islands.name} open at 7pm on Wednesday? {islands.is_open('Wednesday', 19)}")

# Notice how each restaurant has its own data
spudz.update_hours('Monday', 10, 22)
spudz.add_address("456 Potato Ave, Irvine, CA")
print(f"{islands.name} Monday hours: {islands.hours['Monday']}")
print(f"{spudz.name} Monday hours: {spudz.hours['Monday']}")
# This demonstrates how OOP allows us to encapsulate data and behavior related to a restaurant in a single class.


class Student_new:
    def __init__(self, name):
        self.name = name
        self.student_id = ''
        self.gpa = 0.0
    
    def is_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        return False
    
    def update_gpa(self, gpa):
        if 0.0 <= gpa <= 4.0:
            self.gpa = gpa
        else:
            raise ValueError("GPA must be between 0.0 and 4.0")
    
    def set_student_id(self, student_id):
        self.student_id = student_id
    
    def __str__(self):
        honor_status = "Honor Roll" if self.is_honor_roll() else "Not on Honor Roll"
        return f"Name: {self.name}, ID: {self.student_id}, GPA: {self.gpa:.2f}, Status: {honor_status}"

print("Student class created")
# Example usage
student = Student_new("John Doe")
student.set_student_id("12345")
student.update_gpa(3.8)
print(student)  # Display the student information
