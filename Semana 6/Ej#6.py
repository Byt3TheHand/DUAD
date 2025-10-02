def word_fixer(text):
    word_list = text.split("-")
    sorted_list= sorted(word_list)
    final_string = "-".join(sorted_list)

    return final_string


input= "python-variable-funcion-computadora-monitor"
final_text = word_fixer(input)
print(f"{final_text}")
