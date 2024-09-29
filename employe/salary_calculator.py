class SalaryCalculator:
	def calculate_salary(self, employee):
		return employee.hours_worked * employee.hourly_rate

	def calculate_annual_salary(self, employee):
		return self.calculate_salary(employee) * 12

	def calculate_bonus(self, employee):
		return self.calculate_salary(employee) * (1 + employee.bonus_rate)