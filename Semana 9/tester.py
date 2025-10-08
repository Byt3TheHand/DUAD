import csv
with open('student_list.csv', mode='r', newline='', encoding='utf-8') as file:
    reader= csv.DictReader(file)
    for row in reader:
        print(row['Name'])