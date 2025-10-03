
def first_fuction():
    scope_variable = [34, 43,58]
    print(f"{scope_variable[0]}")

scope_variable = [34, 43,58]

def over_50_function():
    for i in scope_variable:
        if i > 50 :
            print(f"Este numero es mayor a 50: {i}") 
        else:
            print(f"Este numero es menor a 50: {i} ")

def main():
    over_50_function()

if __name__ == "__main__":

    main()