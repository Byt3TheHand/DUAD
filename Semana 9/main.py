import csv
     
headers=['Name','Class','Spanish Grade','English Grade','History Grade','Science Grade','Overall Grade']
student_list=[]

with open ('student_list.csv', mode='w', newline='', encoding='utf-8') as f:
    writer= csv.DictWriter(f, fieldnames=headers)
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
    Name= input('Full name of the student :').strip()
    Class= input ('Current Class: ').strip()
    Spanish = int(input('Add Spanish grade: '))
    English= int(input('Add English Grade: '))
    History= int(input('Add History Grade: '))
    Science = int(input('Add Science Grade: '))
    Overall =(Spanish + English + History + Science) / 4



    student = {
        'Name' : Name,
        'Class' : Class,
        'Spanish Grade' : Spanish,
        'English Grade' : English,
        'History Grade' : History,
        'Science Grade' : Science,
        'Overall Grade' : Overall
    
    }

    student_list.append(student)
    
    with open('student_list.csv', mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writerow(student)

    print(f'Student Added : {Name}(Overall:{Overall:.2f})')
        
def view_all_students(student_list):
    print ('\n----- ALL STUDENTS -----\n')
    for s in student_list:
        print(f"{s['Name']} | Class: {s['Class']} | "
              f"Spanish: {s['Spanish Grade']}, English: {s['English Grade']}, "
              f"History: {s['History Grade']}, Science: {s['Science Grade']} | "
              f"Overall: {s['Overall Grade']:.2f}")

      

def main():
    while True:
        op = selection_menu()

        if op == 1:
            add_new_student(student_list)
        elif op == 2:
            view_all_students(student_list)
        elif op == 7:
            break
            
main ()