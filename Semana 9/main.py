import csv
     
headers = ['Name','Class','Spanish Grade','English Grade','History Grade','Science Grade','Overall Grade']


with open('student_list.csv', mode='a', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    if f.tell() == 0: 
        writer.writeheader()

def selection_menu():
    while True:
        try:
            choice = int(input("""\nSelect the operation you want to perform:
1. Add a new student
2. View all indexed students
3. View the top 3 averages
4. View overall average
5. Export students to CSV
6. Import students from CSV
7. Exit
Choose your operation: """))
        except ValueError:
            print("Please enter a valid number between 1 and 7.")
            continue

        if choice not in range(1, 8):
            print("Invalid option. Please choose a number between 1 and 7.")
            continue

        return choice

def add_new_student(student_list):
    Name = input('Full name of the student: ').strip()
    Class = input('Current Class: ').strip()
    Spanish = int(input('Add Spanish grade: '))
    English = int(input('Add English Grade: '))
    History = int(input('Add History Grade: '))
    Science = int(input('Add Science Grade: '))
    Overall = (Spanish + English + History + Science) / 4

    student = {
        'Name': Name,
        'Class': Class,
        'Spanish Grade': Spanish,
        'English Grade': English,
        'History Grade': History,
        'Science Grade': Science,
        'Overall Grade': Overall
    }

    with open('student_list.csv', mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writerow(student)

    print(f"\nStudent added: {Name} (Overall: {Overall:.2f})\n")

def view_all_students():
    print('\n----- ALL STUDENTS -----\n')
    try:
        with open('student_list.csv', mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            empty = True
            for row in reader:
                empty = False
                print(f"{row['Name']} | Class: {row['Class']} | "
                      f"Spanish: {row['Spanish Grade']}, English: {row['English Grade']}, "
                      f"History: {row['History Grade']}, Science: {row['Science Grade']} | "
                      f"Overall: {float(row['Overall Grade']):.2f}")
            if empty:
                print('No students indexed yet.')
    except FileNotFoundError:
        print('No students indexed yet.')


def top3_averages():
    try:
        with open('student_list.csv', mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = []
            for row in reader:
                row['Overall Grade'] = float(row['Overall Grade'])
                rows.append(row)

        if not rows:
            print("No students indexed yet.")
            return

        ordered = sorted(rows, key=lambda r: r['Overall Grade'], reverse=True)
        print("\n--- Top 3 Averages ---")
        for i, r in enumerate(ordered[:3], start=1):
            print(f"{i}. {r['Name']} — {r['Overall Grade']:.2f}")
    except FileNotFoundError:
        print("No students indexed yet.")

def main():
    while True:
        op = selection_menu()

        if op == 1:
            add_new_student(student_list)
        elif op == 2:
            view_all_students()
        elif op == 3:
            top3_averages()
        elif op == 7:
            break

main()
