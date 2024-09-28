from employee import Employee

def main():
    employee        = Employee("Jose Perez", 40, 15)
    salary          = employee.calculate_salary()
    employee_report = employee.generate_report()

    print(employee_report)
    print(f"Salary: {salary}")

main()
