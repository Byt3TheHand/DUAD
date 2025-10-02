new_line = input("Ingrese una nueva linea de texto: ")

with open("new file.txt","a") as new_file:
    new_file.write(new_line + "\n")
    