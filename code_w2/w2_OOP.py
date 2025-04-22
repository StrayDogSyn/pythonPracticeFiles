# Intro to OOP
# Procedural programming is a programming paradigm based on the concept of procedure calls.
# It relies on a sequence of statements to be executed in order.
# In procedural programming, the focus is on writing procedures or functions that operate on data.
restaurants = {
    'name': 'The Gourmet Kitchen',
    'location': '123 Food St, Flavor Town',
    'cuisine': 'Fusion',
    'rating': 4.8,
    'menu': {
        'appetizers': ['Bruschetta', 'Stuffed Mushrooms'],
        'main_courses': ['Grilled Salmon', 'Vegetable Stir Fry'],
        'desserts': ['Chocolate Lava Cake', 'Tiramisu']
    },
    'contact_info': {
        'phone': '555-987-6543',
        'email': '
        'address': {
            'street': '123 Food St',
            'city': 'Flavor Town',
            'state': 'CA',
            'zip': '54321'
        }
    }
}

# Function to update hours of operation
def update_hours(restaurant, new_hours):
    restaurant['hours'] = new_hours
    return restaurant

# Function to check if restaurant is open
def is_open(restaurant, current_time):
    if 'hours' in restaurant:
        open_time, close_time = restaurant['hours']
        return open_time <= current_time <= close_time
    return False
    
# Function to add a new menu item
def add_menu_item(restaurant, category, item):
    if category in restaurant['menu']:
        restaurant['menu'][category].append(item)
    else:
        restaurant['menu'][category] = [item]
    return restaurant
    
# Using the functions
updated_restaurant = update_hours(restaurants, ('10:00 AM', '10:00 PM'))
print("Updated Restaurant Hours:", updated_restaurant['hours'])     

print("Is the restaurant open at 2 PM?", is_open(updated_restaurant, '14:00'))
print("Is the restaurant open at 11 PM?", is_open(updated_restaurant, '23:00'))

