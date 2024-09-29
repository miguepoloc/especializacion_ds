from employe.report_interface import IReport
from gnereic_salary_calculator import GenericSalaryCalculator


class SalaryCalculator(GenericSalaryCalculator, IReport):
	def calculate_salary(self, employee) -> float:
		return employee.hours_worked * employee.hourly_rate

	def calculate_annual_salary(self, employee) -> float:
		return self.calculate_salary(employee) * 12

	def calculate_bonus(self, employee) -> float:
		return self.calculate_salary(employee) * (1 + employee.bonus_rate)

	def generate_report(self, employee, calculated_salary) -> str:
		pass

	def generate_annual_report(self, employee, calculated_salary) -> str:
		pass

	def generate_bonus_report(self, employee, calculated_salary) -> str:
		pass