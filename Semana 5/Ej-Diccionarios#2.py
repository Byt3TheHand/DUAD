entry=int(input("Introduza el numero de Keys & Values que desea ingresar: "))
keys=[]
values=[]

print("Ingrese las llaves")
for i in range(entry):
    key = input(f"Ingrese la clave #{i+1}: ")
    keys.append(key)

print("Ingrese los Valores")
for i in range(entry):
    value = input(f"Ingrese el value {keys[i]}: ")
    values.append(value)
# le agregue una validacion para practicar porque me parecio interesante
if len(keys)==len(values):
    dict = dict(zip(keys, values))
    print("Diccionario Creado:")
    print(dict)
else:
    print("Error")