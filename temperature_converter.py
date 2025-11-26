def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kelvin_to_celsius(k):
    return k - 273.15

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Kelvin to Celsius")

choice = int(input("Enter your choice: "))
value = float(input("Enter temperature: "))

if choice == 1:
    print("Fahrenheit:", celsius_to_fahrenheit(value))
elif choice == 2:
    print("Kelvin:", celsius_to_kelvin(value))
elif choice == 3:
    print("Celsius:", fahrenheit_to_celsius(value))
elif choice == 4:
    print("Celsius:", kelvin_to_celsius(value))
else:
    print("Invalid choice")
