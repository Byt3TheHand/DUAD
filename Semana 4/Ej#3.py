import random

number = random.randint(1,10)
guess_number=int(input("Adivina el numero secreto entre (1 - 10)= "))

while number != guess_number:
    print("No haz adivinado, vuelve a intentarlo")
    guess_number=int(input("Adivina el numero secreto entre (1 - 10)= "))
    
print("Haz adivinado el numero!! Felicidades !!")