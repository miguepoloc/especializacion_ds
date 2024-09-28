from interfaces.bonus_employee_report_interface import IBonusEmployeeReport
from employee_report import EmployeeReport
from bonus_salary_calculator import BonusSalaryCalculator
from interfaces.bonus_salary_calculator_interface import IBonusSalaryCalculator

class BonusEmployeeReport(EmployeeReport, IBonusEmployeeReport):
    def __init__(self, salary_calculator: IBonusSalaryCalculator):
        self.salary_calculator = salary_calculator

    def generate_detailed_report_with_bonus(self, employee, salary_calculator):
        if isinstance(salary_calculator, BonusSalaryCalculator):
            monthly_salary_with_bonus = salary_calculator.calculate_salary_with_bonus(employee)
            annual_salary_with_bonus  = monthly_salary_with_bonus * 12
            return (
                "- Detailed Report With Bonus: \n"
                f"Employee: {employee.name}\n"
                f"Hours Worked: {employee.hours_worked}\n"
                f"Hourly Rate: {employee.hourly_rate}\n"
                f"Monthly Salary with Bonus: {monthly_salary_with_bonus}\n"
                f"Annual Salary with Bonus: {annual_salary_with_bonus}\n"
            )
        else:
            return super().generate_detailed_report(
                employee,
                salary_calculator
            )
