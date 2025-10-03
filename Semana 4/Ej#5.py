approved_grades_count = 0
failed_grades_count = 0
approved_grades_sum = 0
failed_grades_sum = 0
total_grades_sum = 0

total_grades = int(input("Enter the number of grades: "))
grade_counter = 1

while grade_counter <= total_grades:
    print(f"Enter grade number {grade_counter}:")
    current_grade = int(input())  # <--- this was missing indentation in your code
    
    if current_grade < 70:
        failed_grades_count += 1
        failed_grades_sum += current_grade
    else:
        approved_grades_count += 1
        approved_grades_sum += current_grade

    total_grades_sum += current_grade
    grade_counter += 1

if approved_grades_count > 0:
    average_approved = approved_grades_sum // approved_grades_count
else:
    average_approved = 0

if failed_grades_count > 0:
    average_failed = failed_grades_sum // failed_grades_count
else:
    average_failed = 0

if total_grades > 0:
    average_total = total_grades_sum // total_grades
else:
    average_total = 0

print(f"The student has this number of approved grades: {approved_grades_count}")
print(f"This is the average of approved grades: {average_approved}")
print(f"The student has this number of failed grades: {failed_grades_count}")
print(f"This is the average of failed grades: {average_failed}")
print(f"This is the overall average of grades: {average_total}")