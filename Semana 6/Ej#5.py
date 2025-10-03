def upper_and_lower_case_counter():
    upper_count = 0
    lower_count = 0
    text= "HoY es un GRAn dIa"
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count +=1

    return upper_count,  lower_count

upper,lower=upper_and_lower_case_counter()

print(f"There's {upper} Upper case letter and {lower} lower case letters")