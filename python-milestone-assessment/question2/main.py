class Employee:
    def __init__(self, employee_id, name, role, salary):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.salary = float(salary)

    def display_details(self):
        print(f"{self.employee_id} - {self.name} - {self.role} - ₹{self.salary:g}")


def add_employee(employee):
    with open("employees.txt", "a") as file:
        file.write(f"{employee.employee_id},{employee.name},{employee.role},{employee.salary:g}\n")


def read_employees():
    employees = []
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 4:
                    employee = Employee(data[0], data[1], data[2], data[3])
                    employees.append(employee)
    except FileNotFoundError:
        print("Error: employees.txt file not found.")
    return employees


def find_highest_salary(employees):
    if employees:
        return max(employees, key=lambda e: e.salary)
    return None


def find_employees_by_role(employees):
    role_count = {}
    for employee in employees:
        if employee.role in role_count:
            role_count[employee.role] += 1
        else:
            role_count[employee.role] = 1
    return role_count


def main():
    employees = read_employees()
    if not employees:
        return

    print("===== Employee Details =====\n")
    for employee in employees:
        employee.display_details()

    print("\n===== Employees with Salary > 50000 =====\n")
    for employee in employees:
        if employee.salary > 50000:
            print(f"{employee.name} - ₹{employee.salary:g}")

    highest = find_highest_salary(employees)
    if highest:
        print("\nHighest Paid Employee:")
        print(f"{highest.name} - ₹{highest.salary:g}")

    role_count = find_employees_by_role(employees)
    print("\nEmployee Count by Role:")
    for role, count in sorted(role_count.items()):
        print(f"{role}: {count}")


if __name__ == "__main__":
    main()