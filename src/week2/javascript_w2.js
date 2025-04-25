// W2D1 -- Nested Data In-class example

let cart = {
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
    // notice each category is a dictionary with items as keys and quantities as values.
};

// console.log(`Shopping cart contents: ${JSON.stringify(cart)}`);
// console.log(`Total cost: ${cart.total}`);
// Accessing nested data of vegetables.

let veggies = cart['vegetables'];
// console.log(`Vegetables: ${JSON.stringify(veggies)}`);
// console.log('Type:', typeof veggies);

// Get the first fruit key instead of using an index

// let firstFruitKey = Object.keys(cart['fruits'])[0];  // Get the first key from fruits dictionary
// let firstFruitQuantity = cart['fruits'][firstFruitKey];
// console.log(`First fruit: ${firstFruitKey}, quantity: ${firstFruitQuantity}`);

cart['fruits']['kiwi'] = 4;  // Adding a new fruit to the cart
// console.log(`Updated cart: ${JSON.stringify(cart)}`);

cart['other'] = {'snacks': 5};  // Adding a new category to the cart
// console.log(`Updated cart with new category: ${JSON.stringify(cart)}`);

// console.log('All fruits in the cart:');
// Object.entries(cart['fruits']).forEach(([fruit, quantity]) => {
//     console.log(`${fruit}: ${quantity}`);
// });
    
// console.log('All items in the category:');
// Object.entries(cart).forEach(([category, items]) => {
//     if (typeof items === 'object' && items !== null && !Array.isArray(items)) {
//         // Check if the items are an object
//         console.log(`${category.charAt(0).toUpperCase() + category.slice(1)}:`);
//         Object.keys(items).forEach(item => {
//             console.log(`  - ${item}`);
//         });
//         console.log(`${category.charAt(0).toUpperCase() + category.slice(1)}: ${JSON.stringify(items)}`);
//         console.log('//------------------//');
//     }
// });

// Recipe example (converted from Python)
/*
let recipe = {
    "name": "Tofu Stir-Fry",
    "servings": 4,
    "ingredients": {
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

// Build a shopping list from the recipe
console.log(`Ingredients for ${recipe["name"]} (servings: ${recipe["servings"]}):`);

// Print the ingredients by category
for (let [category, items] of Object.entries(recipe['ingredients'])) {
    console.log(`${category.charAt(0).toUpperCase() + category.slice(1)}:`);
    for (let item of items) {
        console.log(`  - ${item}`);
    }
    console.log('//------------------//');
}
*/

// Music library example (converted from Python)
/*
let music_library = {
    "rock": [
        {"title": "Bohemian Rhapsody", "artist": "Queen", "duration": 354},
        {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "duration": 482}
    ],
    "pop": [
        {"title": "Shape of You", "artist": "Ed Sheeran", "duration": 234},
        {"title": "Blinding Lights", "artist": "The Weeknd", "duration": 201}
    ],
    "hip-hop": [
        {"title": "Lose Yourself", "artist": "Eminem", "duration": 326}
    ]
}

// Task 1: Add a new song to the "rock" genre
// Note: The "duration" key in all song dictionaries represents time in seconds.
let new_rock_song = {"title": "Sweet Child O' Mine", "artist": "Guns N' Roses", "duration": 355};
music_library["rock"].push(new_rock_song);
console.log(`Added '${new_rock_song['title']}' by ${new_rock_song['artist']} to the 'Rock' genre`);

// Task 2: Print all songs in the "pop" genre
console.log("\nAll songs in the Pop genre:");
for (let song of music_library["pop"]) {
    console.log(`'${song['title']}' by ${song['artist']} - ${song['duration']} seconds (duration in seconds)`);
}

// Task 3: Calculate the total duration of all songs in "hip-hop"
let total_duration = 0;
for (let song of music_library["hip-hop"]) {
    total_duration += song["duration"];
}
console.log(`\nTotal duration of Hip-hop songs: ${total_duration} seconds.`);
console.log('//------------------//');
*/

// Restaurant example.
// A nested dictionary of restaurants
let restaurants = {
    'Amendolas': {
        'address': '28 Lake St, Monroe, NY 10950',
        'menu_url': 'https://www.amendolaspizzapasta.com/'
    },
    'LaVera Cucina': {
        'address': '43 Hillside Terrace, Monroe, NY 10950',
        'menu_url': 'https://www.veramonroe.com/'
    }
};

// console.log("Restaurant information:");
// console.log(restaurants);

// Accessing Data in Nested Dictionaries:
// Access information about a specific restaurant
let sri_info = restaurants['LaVera Cucina'];
// console.log("LaVera Cucina info:", sri_info);

// Access a specific piece of information
let el_basurero_address = restaurants['Amendolas']['address'];
// console.log("Amendolas address:", el_basurero_address);

// Using get() with a default value for safer access
let el_basurero_phone = restaurants['Amendolas'] && restaurants['Amendolas']['phone'] || 'Not available';
// console.log("Amendolas phone:", el_basurero_phone);

// Modifying Nested Dictionaries:
// Add a new restaurant
restaurants['Joes Pizza'] = {
    'address': '7 Carmine St, New York, NY 10014',
    'phone': '212-366-1182'
};
// console.log("Added Joe's Pizza:", restaurants['Joes Pizza']);

// Add a new field to an existing restaurant
restaurants['Joes Pizza']['menu_url'] = 'http://www.joespizzanyc.com';
// console.log("Updated Joe's Pizza:", restaurants['Joes Pizza']);

// Update an existing field
restaurants['Joes Pizza']['menu_url'] = 'http://www.joespizzanyc.com/menu.php';

// Remove a field
delete restaurants['Joes Pizza']['phone'];
// console.log("Joe's Pizza after removing phone:", restaurants['Joes Pizza']);

/*
// Iterating Through Nested Dictionaries:
// Print all restaurant information in a formatted way
console.log("\nAll Restaurants:");
for (let [restaurant_name, details] of Object.entries(restaurants)) {
    console.log(`\n${restaurant_name}:`);
    for (let [key, value] of Object.entries(details)) {
        console.log(`  ${key}: ${value}`);
    }
    console.log('//------------------//');
}
*/

let inventory = {
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
};

// Print all products with low stock (less than 10)
console.log("\nLow Stock Items:");
for (let [category, subcategories] of Object.entries(inventory)) {
    for (let [subcategory, products] of Object.entries(subcategories)) {
        for (let [product, details] of Object.entries(products)) {
            if (details['stock'] < 10) {
                console.log(`${category} - ${subcategory} - ${product}: Only ${details['stock']} left!`);
            }
        }
    }
}

// Start with this basic structure
let school = {
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
};

// Task 1: Add a new course "CS301: Database Systems" to Computer Science
// taught by "Dr. Lee" with 4 credits
school["Computer Science"]["courses"]["CS301"] = {
    "name": "Database Systems",
    "instructor": "Dr. Lee",
    "credits": 4
};

console.log("\nTask 1: Added new course to Computer Science department");
console.log(`CS301: ${JSON.stringify(school['Computer Science']['courses']['CS301'])}`);
console.log('All courses in Computer Science:');
for (let [course_id, course_info] of Object.entries(school["Computer Science"]["courses"])) {
    console.log(`${course_id}: ${course_info['name']} - ${course_info['credits']} credits`);
    console.log(`  Instructor: ${course_info['instructor']}`);
}

// Task 2: Find and print all courses taught by "Dr. Brown"
console.log("\nTask 2: Courses taught by Dr. Brown:");
for (let [department, dept_info] of Object.entries(school)) {
    let courses = dept_info["courses"];
    for (let [course_id, course_info] of Object.entries(courses)) {
        if (course_info["instructor"] === "Dr. Brown") {
            console.log(`${department} - ${course_id}: ${course_info['name']}`);
        }
    }
}

// Task 3: Print a formatted list of all departments and their courses
console.log("\nTask 3: All Departments and Courses:");
for (let [department, dept_info] of Object.entries(school)) {
    console.log(`\n${department} Department`);
    console.log(`Chair: ${dept_info['chair']}`);
    console.log("Courses:");
    for (let [course_id, course_info] of Object.entries(dept_info["courses"])) {
        console.log(`  ${course_id}: ${course_info['name']} - ${course_info['credits']} credits`);
        console.log(`    Instructor: ${course_info['instructor']}`);
    }
}