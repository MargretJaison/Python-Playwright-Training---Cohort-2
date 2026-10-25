def calculate_grade(average):
    if average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "F"


def calculate_result(student):
    total = student["python"] + student["sql"] + student["ai"]
    average = total / 3
    student["total"] = total
    student["average"] = average
    student["grade"] = calculate_grade(average)
    student["result"] = "PASS" if average >= 40 else "FAIL"


def display_student(student):
    print(f"\nStudent ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Total: {student['total']:g}")
    print(f"Average: {student['average']:g}")
    print(f"Grade: {student['grade']}")
    print(f"Result: {student['result']}")


def main():
    students = []
    number = int(input("Enter number of students: "))

    for i in range(number):
        print(f"\nEnter the details for student {i + 1}")
        student = {
            "id": input("Student ID: "),
            "name": input("Student Name: "),
            "python": float(input("Python Marks: ")),
            "sql": float(input("SQL Marks: ")),
            "ai": float(input("AI Marks: ")),
        }
        calculate_result(student)
        students.append(student)

    if not students:
        print("No students entered.")
        return

    print("\n===== Student Result =====")
    for student in students:
        display_student(student)

    highest_student = max(students, key=lambda s: s["average"])
    print(f"\nHighest Scoring Student: {highest_student['name']}")

    above_75 = [s["name"] for s in students if s["average"] > 75]
    print("Students above 75:", ", ".join(above_75) if above_75 else "None")


if __name__ == "__main__":
    main()