# Ejercicio 2

name = input("What's your name? ")
last_name = input("What's your last name? ")
age = int(input("What's your age? "))

if age < 3:
    category = "a baby"
elif age < 9:
    category = "a child"
elif age < 12:
    category = "a preteen"
elif age < 18:
    category = "a teenager"
elif age < 26:
    category = "a young adult"
elif age < 60:
    category = "an adult"
else:
    category = "a senior"

print(f"{name} {last_name} is {category}.")
