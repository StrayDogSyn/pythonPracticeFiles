# def syntax_error():
#     print("This is a syntax error")
#     # Uncommenting the next line will raise a SyntaxError
#     # print("Hello, world!"
#     # print(dict)

# list_index_error = [1, 2, 3]

# # Fix IndexError by using correct variable and valid index
# list_index_error[2] = 5  # Using valid index

# # Fix TypeError by converting integer to string
# print('me' + str(1))  # Convert int to string

# # Define inventory before using it
# inventory = ['grape', 'apple', 'orange']
# order_1 = ['grape', 'apple']

# def check_order(order):
#     for item in order:
#         if item not in inventory:
#             return False
# print(check_order(order_1))
# # Remove the hardcoded output

        
# print(check_order(order_1))
# True
# def check_order(order):
#     for item in order:
#         if item not in inventory:
#             print('Item is in order: ', item)
#             return False
#         else:
#             return True

        
# print(check_order(order_1))
# True
# print(check_order(order_2))
# # Remove the hardcoded output

# print(check_order(order_2))
# Item is in order:  pineapple
# def check_order_2(order):
#     for item in order:
#         print('The item exists:', item)
#         if item not in inventory:  # Fix syntax error (removed 'is')
#             print('Exit loop, found bad item')
#             return False
#         if item is not in inventory:
            
# SyntaxError: invalid syntax
# def check_order_2(order):
#     for item in order:
#         print('The item exists:', item)
#         if item not in inventory:
#             print('Exit loop, found bad item')
#             return False

        
# def check_order_2(order):
#     for item in order:
#         print('The item exists:', item)
#         if item not in inventory:
#             print('Exit loop, found bad item')
#             return False

#     return True

# order = []
# print(check_order_2)
# <function check_order_2 at 0x0000014FCFC74D60>
# print(check_order_2(order_2))
# The item exists: pineapple
# Exit loop, found bad item
# False
# # Soo many errors...

# # Simulating a do-while loop in Python
# inventory_check = True
# order_3 = ['apple', 'pineapple', 'orange']

# print("Checking order using a simulated do-while loop:")
# i = 0
# while True:
#     item = order_3[i]
#     print(f"Checking item: {item}")
    
#     if item not in inventory:
#         print(f"Item not available: {item}")
#         inventory_check = False
#         break
    
#     i += 1
#     if i >= len(order_3):
#         break

# print(f"Order check result: {inventory_check}")

# inventory_dict = {1: 'apple', 2: 'kiwi', 3: 'banana', 4: 'orange', 5: 'grape', 6: 'pear'}

# try:
#     user_input = input("Enter a number: ")
    
#     # Try to convert input to integer if it's a digit
#     if user_input.isdigit():
#         user_input = int(user_input)
        
#     # Access the dictionary with the key
#     if user_input in inventory_dict:
#         print(f"Found: {inventory_dict[user_input]}")
#     else:
#         print(f"Fruit '{user_input}' not found in inventory")
# except Exception as e:
#     print(f"An error occurred: {e}")
# # except ValueError as ve:
# #     print(f"Value error: {ve}")
# # except KeyError as ke:
# #     print(f"Key error: {ke}")
# # except TypeError as te:
# #     print(f"Type error: {te}")
# # except IndexError as ie:
# #     print(f"Index error: {ie}")
# # except SyntaxError as se:
# #     print(f"Syntax error: {se}")
# # except NameError as ne:
# #     print(f"Name error: {ne}")
# else:
#     print("No exceptions occurred")
# finally:
#     print("Bye Felica!")
# # # Example of raising an exception


def divide_inputs(input1, input2):
    """
    Divides two numeric inputs.

    Args:
        input1 (float): The numerator.
        input2 (float): The denominator.

    Returns:
        float: The result of the division.

    Raises:
        ValueError: If the denominator is zero.
        TypeError: If the inputs are not numeric.
        IndexError: If the inputs are not provided.
        SyntaxError: If the inputs are not valid numbers.
        ZeroDivisionError: If the denominator is zero.
    """
    num1 = float(input1)
    num2 = float(input2)
    if num2 == 0:
        raise ValueError("Division by zero is not allowed.")
    return num1 / num2

def get_inputs():
    try:
        input1 = input("Enter the first number: ")
        input2 = input("Enter the second number: ")
        result = divide_inputs(input1, input2)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as te:
        print(f"Type error: {te}")
    except IndexError as ie:
        print(f"Index error: {ie}")
    except SyntaxError as se:
        print(f"Syntax error: {se}")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    finally:
        print("Bye Felica!")
# Execute the function to get user inputs
get_inputs()

