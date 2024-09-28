from interfaces.salary_calculator_interface import ISalaryCalculator

class SalaryCalculator(ISalaryCalculator):
    def calculate_salary(self, employee):
        return employee.hours_worked * employee.hourly_rate

    def calculate_annual_salary(self, employee):
        return self.calculate_salary(employee) * 52
