example = ["Hola\n", "mundo\n", "esto\n", "es\n", "Python\n"]

with open("salutation.txt", "w") as file:
    file.writelines(example)

with open("salutation.txt","r") as new_file:
    salutation = new_file.readlines()

lines_to_String =" ".join(salutation)
string_to_list = lines_to_String.split()
number = len(string_to_list)

print(number)

# esto explica mejor cada movimiento,.readlines me da una lista de lineas, con los marcadores de reglon, luego tomamos esa lista 
# y la pasamos a un string largo, y luego a ese string lo pasamos a una lista de palabras, len() lee la cantidad de palabras retornando el 
# numero

from_list_of_lines_to_String =" ".join(salutation)
from_string_to_list_of_words = from_list_of_lines_to_String.split()
number = len(from_string_to_list_of_words)
