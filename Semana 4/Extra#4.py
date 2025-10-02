number = []
first = int(input("Digite su primer dígito (1 / 2) = "))
second = int(input("Digite su segundo dígito (2 / 2) = "))
number.append(first)
number.append(second)

if number[0] > number[1]:
    print(f"{number[0]} es el mayor y {number[1]} es el menor")
else:
    print(f"{number[1]} es el mayor y {number[0]} es el menor")
