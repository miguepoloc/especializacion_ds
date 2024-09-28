from interfaces.employee_report_interface import IEmployeeReport
from interfaces.salary_calculator_interface import ISalaryCalculator

class EmployeeReport(IEmployeeReport):
    def __init__(self, salary_calculator: ISalaryCalculator):
        self.__salary_calculator = salary_calculator

    def generate_report(self, employee):
        return (
            "- Employee Report: "
            f"Employee: {employee.name}, "
            f"Hours Worked: {employee.hours_worked}, "
            f"Hourly Rate: {employee.hourly_rate}\n"
        )

    def generate_detailed_report(self, employee):
        monthly_salary = self.__salary_calculator.calculate_salary(employee)
        annual_salary  = self.__salary_calculator.calculate_annual_salary(employee)
        return (
            "- Deatil Employee Report: \n"
            f"Employee: {employee.name}\n"
            f"Hours Worked: {employee.hours_worked}\n"
            f"Hourly Rate: {employee.hourly_rate}\n"
            f"Monthly Salary: {monthly_salary}\n"
            f"Annual Salary: {annual_salary}\n"
        )
