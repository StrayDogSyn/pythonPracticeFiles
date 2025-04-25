# Convert room temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

# Convert room temperature from Celsius to Fahrenheit
room_temp_c = 22
room_temp_f = celsius_to_fahrenheit(room_temp_c)
print(f"Room temperature: {room_temp_c}°C is {room_temp_f}°F")
# Convert outdoor temperature from Celsius to Fahrenheit
outdoor_temp_c = 15
outdoor_temp_f = celsius_to_fahrenheit(outdoor_temp_c)
print(f"Outdoor temperature: {outdoor_temp_c}°C is {outdoor_temp_f}°F")
# Convert body temperature from Celsius to Fahrenheit
body_temp_c = 37
body_temp_f = celsius_to_fahrenheit(body_temp_c)
print(f"Body temperature: {body_temp_c}°C is {body_temp_f}°F")
