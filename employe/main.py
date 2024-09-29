from employee import Employee
from salary_calculator import SalaryCalculator
from report_generator import ReportGenerator

def main():
    employee = Employee("Jose Perez", 40, 25, 0.10)
    salary_calculator = SalaryCalculator()
    report_generator = ReportGenerator()

    calculated_salary = salary_calculator.calculate_salary(employee)

    print(report_generator.generate_report(employee=employee))
    print(f"Calculated Salary: {calculated_salary}")

main()
