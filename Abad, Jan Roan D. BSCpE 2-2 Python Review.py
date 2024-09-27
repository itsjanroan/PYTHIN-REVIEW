# CREATOR INFORMATION 
# Name: Abad, Jan Roan D. 
# Subject: Data Structure and Algorithm - "Python Review Exercise No. 1"
# Section: BSCpE 2-2

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature():
    try:
        temperature = float(input("Enter the temperature you'd like to convert: "))
        conversion_choice = input("Would you like to convert:\nA. Celsius to Fahrenheit\nB. Fahrenheit to Celsius\nChoose A or B: ").strip().upper()

        if conversion_choice == "A":
            result = celsius_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {result:.2f}°F")
        elif conversion_choice == "B":
            result = fahrenheit_to_celsius(temperature)
            print(f"{temperature}°F is equal to {result:.2f}°C")
        else:
            print("Invalid choice. Please select 'A' or 'B'.")
    except ValueError:
        print("Please enter a valid numerical temperature.")


# CREATOR INFORMATION 
# Name: Abad, Jan Roan D. 
# Subject: Data Structure and Algorithm - "Python Review Exercise No. 2"
# Section: BSCpE 2-2

def calculate_voltage(current, resistance):
    return current * resistance

def calculate_current(voltage, resistance):
    return voltage / resistance

def calculate_resistance(voltage, current):
    return voltage / current

def ohms_law_calculator():
    print("What would you like to calculate?")
    print("1. Voltage (V)")
    print("2. Current (I)")
    print("3. Resistance (R)")

    choice = input("Enter 1, 2, or 3: ").strip()

    try:
        if choice == "1":
            current = float(input("Enter the current (I) in amperes: "))
            resistance = float(input("Enter the resistance (R) in ohms: "))
            voltage = calculate_voltage(current, resistance)
            print(f"The voltage is {voltage:.2f} volts.")
        elif choice == "2":
            voltage = float(input("Enter the voltage (V) in volts: "))
            resistance = float(input("Enter the resistance (R) in ohms: "))
            if resistance == 0:
                print("Resistance cannot be zero. Please enter a valid resistance value.")
            else:
                current = calculate_current(voltage, resistance)
                print(f"The current is {current:.2f} amperes.")
        elif choice == "3":
            voltage = float(input("Enter the voltage (V) in volts: "))
            current = float(input("Enter the current (I) in amperes: "))
            if current == 0:
                print("Current cannot be zero. Please enter a valid current value.")
            else:
                resistance = calculate_resistance(voltage, current)
                print(f"The resistance is {resistance:.2f} ohms.")
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")
    except ValueError:
        print("Please ensure you're entering valid numbers.")


# CREATOR INFORMATION 
# Name: Abad, Jan Roan D. 
# Subject: Data Structure and Algorithm - "Python Review Exercise No. 3"
# Section: BSCpE 2-2 

def print_diamond(size):
    if size % 2 == 0:
        return "Please provide an odd number for a symmetrical diamond."

    # Print the upper half of the diamond
    for i in range(size // 2 + 1):
        print(' ' * (size // 2 - i) + '*' * (2 * i + 1))
    
    # Print the lower half of the diamond
    for i in range(size // 2 - 1, -1, -1):
        print(' ' * (size // 2 - i) + '*' * (2 * i + 1))


# Main Menu
def main_menu():
    while True:
        print("\nSelect an option:")
        print("1. Input a temperature and convert it")
        print("2. Calculate using Ohm's Law")
        print("3. Print a diamond pattern")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            convert_temperature()
        elif choice == "2":
            ohms_law_calculator()
        elif choice == "3":
            try:
                size = int(input("Enter an odd number to print a diamond: "))
                result = print_diamond(size)
                if result:
                    print(result)
            except ValueError:
                print("Please enter a valid integer.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

        continue_choice = input("Do you want to return to the main menu? (yes/no): ").strip().lower()
        if continue_choice != "yes":
            break

main_menu()
