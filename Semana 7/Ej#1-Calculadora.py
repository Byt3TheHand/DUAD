def initial_number():
    while True:
        try:
            return int(input("Enter the initial number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def selection_menu(current_number):
    while True:
        try:
            operation_selection = int(input(f'''\nSelect the operation you want to perform on your number {current_number}:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Clear Result
6. Exit Calculator
Choose your operation: '''))
        except ValueError:
            print("Please enter a valid number between 1 and 6.")
            continue

        if operation_selection not in (1, 2, 3, 4, 5, 6):
            print("Invalid option. Please choose a number between 1 and 6.")
            continue

        return operation_selection

def perform_operation(selection, current_number):
    if selection == 1:
        try:
            n = float(input("Number to add: "))
            current_number += n
            print(f"Now: {current_number}")
        except ValueError:
            print("Invalid number.")

    elif selection == 2:
        try:
            n = float(input("Number to subtract: "))
            current_number -= n
            print(f"Now: {current_number}")
        except ValueError:
            print("Invalid number.")

    elif selection == 3:
        try:
            n = float(input("Number to multiply by: "))
            current_number *= n
            print(f"Now: {current_number}")
        except ValueError:
            print("Invalid number.")

    elif selection == 4:
        try:
            n = float(input("Number to divide by: "))
            if n == 0:
                print("Cannot divide by zero.")
            else:
                current_number /= n
                print(f"Now: {current_number}")
        except ValueError:
            print("Invalid number.")

    elif selection == 5:
        current_number = 0
        print("Result cleared. The number is now 0.")

    elif selection == 6:
        print("Exiting calculator.")
        return None

    return current_number 

def main():
    current_number = initial_number()

    while True:
        selection = selection_menu(current_number)
        result = perform_operation(selection, current_number)
        if result is None:
            break
        else:
            current_number = result

if __name__ == "__main__":
    main()

