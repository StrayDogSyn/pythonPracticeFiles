# W2D1 -- Nested Data In-class example

cart = {
    'fruits': {
        'apple': 2,
        'banana': 3,
        'orange': 5
    },
    'vegetables': {
        'carrot': 4,
        'broccoli': 2,
        'spinach': 1
    },
    'dairy': {
        'milk': 1,
        'cheese': 2,
        'yogurt': 3
    },
    'total': 24.74
# notice each category is a dictionary with items as keys and quantities as values.
}

# print(f'Shopping cart contents: {cart}')
# print(f'Total cost: {cart["total"]}')
# Accessing nested data of vegetables.

veggies = cart['vegetables']
# print(f'Vegetables: {veggies}')
# print('Type:', type(veggies))

# Get the first fruit key instead of using an index

# first_fruit_key = list(cart['fruits'].keys())[0]  # Get the first key from fruits dictionary
# first_fruit_quantity = cart['fruits'][first_fruit_key]
# print(f'First fruit: {first_fruit_key}, quantity: {first_fruit_quantity}')

cart['fruits']['kiwi'] = 4  # Adding a new fruit to the cart
# print(f'Updated cart: {cart}')

cart['other'] = {'snacks': 5}  # Adding a new category to the cart
# print(f'Updated cart with new category: {cart}')

# print('All fruits in the cart:')
# for fruit, quantity in cart['fruits'].items():
#     print(f'{fruit}: {quantity}')
    
# print('All items in the category:')
# for category, items in cart.items():
#     if isinstance(items, dict):
#         # Check if the items are a dictionary
#         print(f'{category.title()}:')
#         for item in items:
#             print(f'  - {item}') 
#         print(f'{category.title()}: {items}')
#         print('//------------------//')
# On to recipe example

# A recipe with ingredients organized by category
# recipe = {
#     'name': 'Vegetable Stir Fry',
#     'prep_time': 15,
#     'cook_time': 10,
#     'servings': 4,
#     'ingredients': {
#         'proteins': ['tofu', 'cashews'],
#         'vegetables': ['bell pepper', 'broccoli', 'carrot', 'snow peas'],
#         'aromatics': ['garlic', 'ginger', 'green onion'],
#         'sauce': ['soy sauce', 'sesame oil', 'corn starch']
#     },
#     'steps': [
#         'Press and cube tofu',
#         'Chop all vegetables',
#         'Mix sauce ingredients',
#         'Stir-fry aromatics',
#         'Add vegetables and tofu',
#         'Add sauce and simmer'
#     ]
# }
# # Build a shopping list from the recipe

# print(f'Ingredients for {recipe["name"]}(servings: {recipe["servings"]}):')

# # Print the ingredients by category
# for category, items in recipe['ingredients'].items():
#     print(f'{category.title()}:')
#     for item in items:
#         print(f'  - {item}')
#     print('//------------------//')

# # Start with this basic structure
# music_library = {
#     "rock": [
#         {"title": "Bohemian Rhapsody", "artist": "Queen", "duration": 354},
#         {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "duration": 482}
#     ],
#     "pop": [
#         {"title": "Shape of You", "artist": "Ed Sheeran", "duration": 234},
#         {"title": "Blinding Lights", "artist": "The Weeknd", "duration": 201}
#     ],
#     "hip-hop": [
#         {"title": "Lose Yourself", "artist": "Eminem", "duration": 326}
#     ]
# }

# # Task 1: Add a new song to the "rock" genre
# # Note: The "duration" key in all song dictionaries represents time in seconds.

# new_rock_song = {"title": "Sweet Child O' Mine", "artist": "Guns N' Roses", "duration": 355}

# print(f"Added '{new_rock_song['title']}' by {new_rock_song['artist']} to the 'Rock' genre")


# # Task 2: Print all songs in the "pop" genre
# print("\nAll songs in the Pop genre:")
# for song in music_library["pop"]:
#     print(f"'{song['title']}' by {song['artist']} - {song['duration']} seconds (duration in seconds)")

# # Task 3: Calculate the total duration of all songs in "hip-hop"
# total_duration = 0
# for song in music_library["hip-hop"]:
#     total_duration += song["duration"]
# print(f"\nTotal duration of Hip-hop songs: {total_duration} seconds.")
# print('//------------------//')

# Restaurant example.
# A nested dictionary of restaurants
restaurants = {
    'Amendolas': {
        'address': '28 Lake St, Monroe, NY 10950',
          'menu_url': 'https://www.amendolaspizzapasta.com/'
    },
    'LaVera Cucina': {
        'address': '43 Hillside Terrace, Monroe, NY 10950',
        'menu_url': 'https://www.veramonroe.com/'
    }
}
# print("Restaurant information:")
# print(restaurants)
# Accessing Data in Nested Dictionaries:
# Access information about a specific restaurant
sri_info = restaurants['LaVera Cucina']
# print("LaVera Cucina info:", sri_info)
# Access a specific piece of information
el_basurero_address = restaurants['Amendolas']['address']
# print("Amendolas address:", el_basurero_address)
# Using get() with a default value for safer access
el_basurero_phone = restaurants.get('Amendolas', {}).get('phone', 'Not available')
# print("Amendolas phone:", el_basurero_phone)
# Modifying Nested Dictionaries:
# Add a new restaurant
restaurants['Joes Pizza'] = {
    'address': '7 Carmine St, New York, NY 10014',
    'phone': '212-366-1182'
}
# print("Added Joe's Pizza:", restaurants['Joes Pizza'])
# Add a new field to an existing restaurant
restaurants['Joes Pizza']['menu_url'] = 'http://www.joespizzanyc.com'
# print("Updated Joe's Pizza:", restaurants['Joes Pizza'])
# Update an existing field
restaurants['Joes Pizza']['menu_url'] = 'http://www.joespizzanyc.com/menu.php'
# Remove a field
restaurants['Joes Pizza'].pop('phone')
# print("Joe's Pizza after removing phone:", restaurants['Joes Pizza'])
# Iterating Through Nested Dictionaries:
# Print all restaurant information in a formatted way
# print("\nAll Restaurants:")
# for restaurant_name, details in restaurants.items():
#     print(f"\n{restaurant_name}:")
#     for key, value in details.items():
#         print(f"  {key}: {value}")
#         print('//------------------//')
        
# Accessing a specific restaurant's information
# amendolas_info = restaurants.get('Amendolas', {})
# print("Amendolas info:", amendolas_info)
# amendolas_phone = amendolas_info.get('phone', 'Not available')
# print("Amendolas phone:", amendolas_phone)

# restaurants['Joes Pizza'] = {
#     'address': '7 Carmine St, New York, NY 10014',
#     'phone': '212-366-1182'
# }
# print(restaurants)
# restaurants['Joes Pizza']['menu_url'] = 'http://www.joespizzanyc.com'
# print(restaurants['Joes Pizza'])

# restaurants['Joes Pizza'].pop('phone')
# print(restaurants['Joes Pizza'])
# # print('//------------------//')
# print('All Restaurants:')
# for restaurant_name, details in restaurants.items():
#     print(f"\n{restaurant_name}:")
#     for key, value in details.items():
#         print(f"  {key}: {value}")
#         print('//------------------//')
        

inventory = {
    'electronics': {
        'smartphones': {
            'iPhone 13': {'price': 799, 'stock': 15, 'colors': ['black', 'white', 'red']},
            'Samsung Galaxy S21': {'price': 699, 'stock': 10, 'colors': ['black', 'silver']}
        },
        'laptops': {
            'MacBook Pro': {'price': 1299, 'stock': 5, 'specs': {'ram': '16GB', 'storage': '512GB'}},
            'Dell XPS': {'price': 999, 'stock': 8, 'specs': {'ram': '8GB', 'storage': '256GB'}}
        }
    },
    'clothing': {
        't-shirts': {
            'Basic Tee': {'price': 19.99, 'stock': 50, 'sizes': ['S', 'M', 'L', 'XL']},
            'Graphic Tee': {'price': 24.99, 'stock': 35, 'sizes': ['M', 'L']}
        }
    }
}

# Print all products with low stock (less than 10)
print("\nLow Stock Items:")
for category, subcategories in inventory.items():
    for subcategory, products in subcategories.items():
        for product, details in products.items():
            if details['stock'] < 10:
                print(f"{category} - {subcategory} - {product}: Only {details['stock']} left!")

# Start with this basic structure
school = {
    "Computer Science": {
        "chair": "Dr. Jane Smith",
        "courses": {
            "CS101": {"name": "Intro to Programming", "instructor": "Dr. Brown", "credits": 3},
            "CS201": {"name": "Data Structures", "instructor": "Dr. Green", "credits": 4}
        }
    },
    "Mathematics": {
        "chair": "Dr. Tom Johnson",
        "courses": {
            "MATH101": {"name": "Calculus I", "instructor": "Dr. White", "credits": 4},
            "MATH205": {"name": "Linear Algebra", "instructor": "Dr. Brown", "credits": 3}
        }
    }
}

# Task 1: Add a new course "CS301: Database Systems" to Computer Science
# taught by "Dr. Lee" with 4 credits
school["Computer Science"]["courses"]["CS301"] = {
    "name": "Database Systems",
    "instructor": "Dr. Lee",
    "credits": 4
}
print("\nTask 1: Added new course to Computer Science department")
print(f"CS301: {school['Computer Science']['courses']['CS301']}")
print('All courses in Computer Science:')
for course_id, course_info in school["Computer Science"]["courses"].items():
    print(f"{course_id}: {course_info['name']} - {course_info['credits']} credits")
    print(f"  Instructor: {course_info['instructor']}")
# Task 2: Find and print all courses taught by "Dr. Brown"
print("\nTask 2: Courses taught by Dr. Brown:")
for department, dept_info in school.items():
    courses = dept_info["courses"]
    for course_id, course_info in courses.items():
        if course_info["instructor"] == "Dr. Brown":
            print(f"{department} - {course_id}: {course_info['name']}")

# Task 3: Print a formatted list of all departments and their courses
print("\nTask 3: All Departments and Courses:")
for department, dept_info in school.items():
    print(f"\n{department} Department")
    print(f"Chair: {dept_info['chair']}")
    print("Courses:")
    for course_id, course_info in dept_info["courses"].items():
        print(f"  {course_id}: {course_info['name']} - {course_info['credits']} credits")
        print(f"    Instructor: {course_info['instructor']}")