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
    
print('All items in the category:')
for category, items in cart.items():
    if isinstance(items, dict):
        # Check if the items are a dictionary
        print(f'{category.title()}:')
        for item in items:
            print(f'  - {item}') 
        print(f'{category.title()}: {items}')
        print('------------------')
# On to recipe example

# A recipe with ingredients organized by category
recipe = {
    'name': 'Vegetable Stir Fry',
    'prep_time': 15,
    'cook_time': 10,
    'servings': 4,
    'ingredients': {
        'proteins': ['tofu', 'cashews'],
        'vegetables': ['bell pepper', 'broccoli', 'carrot', 'snow peas'],
        'aromatics': ['garlic', 'ginger', 'green onion'],
        'sauce': ['soy sauce', 'sesame oil', 'corn starch']
    },
    'steps': [
        'Press and cube tofu',
        'Chop all vegetables',
        'Mix sauce ingredients',
        'Stir-fry aromatics',
        'Add vegetables and tofu',
        'Add sauce and simmer'
    ]
}
# Build a shopping list from the recipe

print(f'Ingredients for {recipe["name"]}(servings: {recipe["servings"]}):')

for category, items in recipe['ingredients'].items():
    print(f'{category.title()}:')
    for item in items:
        print(f'  - {item}')
    print('------------------')
    
    









