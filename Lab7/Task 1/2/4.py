def find_second_lowest_students():
    students = []  # List to store student name and grade

    # Read the number of students
    n = int(input().strip())

    # Read student names and grades
    for _ in range(n):
        name = input().strip()
        grade = float(input().strip())
        students.append([name, grade])

    # Extract unique grades and sort them
    unique_grades = sorted(set(grade for _, grade in students))
    
    # Find the second lowest grade
    second_lowest_grade = unique_grades[1]

    # Find students with the second lowest grade and sort their names alphabetically
    second_lowest_students = sorted([name for name, grade in students if grade == second_lowest_grade])

    # Print the names of students with the second lowest grade
    for student in second_lowest_students:
        print(student)

# Call the function
find_second_lowest_students()
