from gnereic_salary_calculator import GenericSalaryCalculator

class SalaryCalculator(GenericSalaryCalculator):
	def calculate_salary(self, employee) -> float:
		return employee.hours_worked * employee.hourly_rate

	def calculate_annual_salary(self, employee) -> float:
		return self.calculate_salary(employee) * 12

	def calculate_bonus(self, employee) -> float:
		return self.calculate_salary(employee) * (1 + employee.bonus_rate)