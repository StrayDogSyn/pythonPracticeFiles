def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32

def display_temperature(location, temp_c):
    """
    Display temperature conversion for a given location.
    
    Args:
        location (str): Description of the temperature location
        temp_c (float): Temperature in Celsius
    """
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"{location}: {temp_c}°C is {temp_f:.1f}°F")

# Temperature conversions for different scenarios
temperatures = {
    "Room temperature": 22,
    "Outdoor temperature": 15,
    "Body temperature": 37
}

# Display all temperature conversions
for location, temp_c in temperatures.items():
    display_temperature(location, temp_c)
