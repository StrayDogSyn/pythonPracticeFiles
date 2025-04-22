# OOP approach using a Restaurant class
class Restaurant:
    """A class to represent a restaurant with its details."""
    
    def __init__(self, name):
        """Initialize a restaurant with a name and default values."""
        self.name = name
        self.addresses = []
        self.menu_url = ''
        self.hours = {
            'Sunday': [0, 0],
            'Monday': [0, 0],
            'Tuesday': [0, 0],
            'Wednesday': [0, 0],
            'Thursday': [0, 0],
            'Friday': [0, 0],
            'Saturday': [0, 0],
        }
    
    def update_hours(self, day, opening, closing):
        """Update the opening and closing hours for a specific day."""
        hours_for_day = self.hours[day]
        hours_for_day[0] = opening
        hours_for_day[1] = closing
    
    def is_open(self, day, time):
        """Check if the restaurant is open at a specific time on a specific day."""
        hours_for_day = self.hours[day]
        return hours_for_day[0] < time < hours_for_day[1]

# Creating a restaurant using our class
islands = Restaurant('Islands')
spudz = Restaurant('Spudz')

# Using the methods
islands.update_hours('Wednesday', 8, 17)
print(islands.hours)
print(f"Is {islands.name} open at noon on Wednesday? {islands.is_open('Wednesday', 12)}")
print(f"Is {islands.name} open at 7pm on Wednesday? {islands.is_open('Wednesday', 19)}")

# Notice how each restaurant has its own data
spudz.update_hours('Monday', 10, 22)
print(f"{islands.name} Monday hours: {islands.hours['Monday']}")
print(f"{spudz.name} Monday hours: {spudz.hours['Monday']}")
# This demonstrates how OOP allows us to encapsulate data and behavior related to a restaurant in a single class.
