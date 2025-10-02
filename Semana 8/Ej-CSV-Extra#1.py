import csv

with open("gameclass.csv", mode="r", newline= "",encoding="utf-8") as file :
    reader=csv.reader(file)
    
    for row in reader:
        print(f"Nombre: {row[0]}")
        print(f"Género: {row[1]}")
        print(f"Desarrollador: {row[2]}")
        print(f"Clasificación: {row[3]}\n")