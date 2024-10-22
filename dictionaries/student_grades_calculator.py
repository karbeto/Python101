# You need to use .items() if you work with dict
students_grades = {
    "Kristijan": [85, 92, 78],
    "Antonio": [90, 88, 95],
    "Sashe": [80, 70, 65]
}


def get_average_students_grades(students):
    for student, grades in students.items():
        average_grade = sum(grades) / len(grades)
        print(f"{student}: {average_grade:.2f}")


get_average_students_grades(students_grades)
