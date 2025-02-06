def fahrenheit_into_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

fahrenheit = float(input(": "))
print(f"Converted Fahrenheit into the Celsius: {fahrenheit_into_celsius(fahrenheit):.2f}")
