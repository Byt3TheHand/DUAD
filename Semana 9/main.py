import csv

# -- Costants --

HEADERS = ['Name','Class','Spanish Grade','English Grade','History Grade','Science Grade','Overall Grade']
FILE_PATH = 'student_list.csv'

# --- Local Memory ---
student_list =[] # lista global

# --- CSV Headers Creation ---
with open(FILE_PATH , mode='a', newline='',encoding='utf-8') as f:
    writer = csv.DictWriter(f,fieldnames=HEADERS)
    if f.tell() == 0:
        writer.writeheader()

# --- Funcion 1 - Menu ---

def selection_menu():
    while True:
        try:
            choice= int(input("""\nSeleciona la operacion que deseas realizar :
1. Agregar un estudiante nuevo
2. Ver la lista total de estudiantes
3. Ver los primeros 3 promedios
4. Ver el promedio general de todos los estudiantes
5. Exportar la lista de estudiantes
6. Importar una lista de estudiantes
7. Salir del programa
Seleccione una opcion: """))
          
        except ValueError:
            print ('Favot ingresar un numero valido entre 1 y 7.')
            continue
        
        if choice not in range(1,8):
            print ('Número incalido. Favor ingresa un numero entre 1 y 7.')
            continue
        
        return choice
    
selection_menu ()