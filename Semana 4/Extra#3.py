initial_number = int(input("Digite un número entre 1 - 10: "))
counter = 1
sum_of_numbers = 0

while counter <= initial_number:
    sum_of_numbers += counter
    counter += 1

print(f"La suma progresiva hasta su número, empezando desde uno hasta {initial_number}, es: {sum_of_numbers}")
