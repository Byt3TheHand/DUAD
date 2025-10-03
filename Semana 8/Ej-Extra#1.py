example = ["Hola\n", "mundo\n", "esto\n", "es\n", "Python\n"]

with open("salutation.txt", "w") as file:
    file.writelines(example)

with open("salutation.txt","r") as new_file:
    salutation = new_file.readlines()

salutation = [salute.strip() for salute in salutation]
result = " ".join(salutation)

print(result)
