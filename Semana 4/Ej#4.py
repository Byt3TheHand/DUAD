number_list = []
input_counter = 0
max_counter = 3

while input_counter < max_counter:
    number = int(input(f"Ingrese el número {input_counter + 1} / {max_counter}: "))
    number_list.append(number)
    input_counter += 1

max_value = number_list[0]

for i in range(1, max_counter):
    if number_list[i] > max_value:
        max_value = number_list[i]

print(f"El número más alto es {max_value}")
