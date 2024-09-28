from employee import Employee
from salary_calculator import SalaryCalculator
from employee_report import EmployeeReport

def main():
    employee   = Employee("Jose Prez", 40, 15)
    calculator = SalaryCalculator()
    report     = EmployeeReport()

    salary          = calculator.calculate_salary(employee)
    employee_report = report.generate_report(employee)

    print(employee_report)
    print(f"Salary: {salary}")

main()
