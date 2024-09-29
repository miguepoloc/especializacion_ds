from employee import Employee

def main():
    employee = Employee("John Doe", 40, 25, 0.10)
    print(employee.generate_report())
    print(employee.generate_detailed_report())
    print(employee.generate_detailed_report_with_bonus())

main()
