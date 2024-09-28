from employee import Employee
from salary_calculator import SalaryCalculator
from employee_report import EmployeeReport
from bonus_salary_calculator import BonusSalaryCalculator
from bonus_employee_report import BonusEmployeeReport

def main():
    employee         = Employee("Jose Prez", 40, 15)
    calculator       = SalaryCalculator()
    bonus_calculator = BonusSalaryCalculator(bonus_rate=0.1)
    report           = EmployeeReport()
    bonus_report     = BonusEmployeeReport()

    employee.update_hours_worked(5)
    employee.update_hourly_rate(20)

    salary            = calculator.calculate_salary(employee)
    annual_salary     = calculator.calculate_annual_salary(employee)
    salary_with_bonus = bonus_calculator.calculate_salary_with_bonus(employee)

    employee_report            = report.generate_report(employee)
    detailed_report            = report.generate_detailed_report(employee, calculator)
    detailed_report_with_bonus = bonus_report.generate_detailed_report_with_bonus(employee, bonus_calculator)

    print(f"Salary with Bonus: {salary_with_bonus}")
    print(f"Salary: {salary}")
    print(f"Annual Salary: {annual_salary}")
    print(employee_report)
    print(detailed_report)
    print(detailed_report_with_bonus)

main()
