# Taking two numbers from the user
RAJESH = float(input("Enter first number: "))
HAZRA = float(input("Enter second number: "))


# Performing operations
addition = RAJESH + HAZRA
subtraction = RAJESH - HAZRA
multiplication = RAJESH * HAZRA

# Checking division by zero
if HAZRA != 0:
    division = RAJESH / HAZRA
else:
    division = "Cannot divide by zero"

# Displaying results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
