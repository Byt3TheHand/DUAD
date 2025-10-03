counter = 1
my_list = []

while counter <= 10:
    num = int(input(f"Ingrese su dígito ({counter} / 10): "))
    my_list.append(num)
    counter += 1

mayor = my_list[0]
for num in my_list:
    if num > mayor:
        mayor = num

print(f"Lista ingresada: {my_list}. El número más alto es: {mayor}.")