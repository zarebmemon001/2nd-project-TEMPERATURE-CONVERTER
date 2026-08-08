print("===== TEMPERATURE CONVERTER =====")

# Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit_answer = (celsius * 9 / 5) + 32

print(celsius, "Celsius is equal to", fahrenheit_answer, "Fahrenheit")


# Fahrenheit to Celsius
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius_answer = (fahrenheit - 32) * 5 / 9

print(fahrenheit, "Fahrenheit is equal to", celsius_answer, "Celsius")