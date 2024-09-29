class ReportGenerator:
	def generate_report(self, employee, calculated_salary) -> str:
		return (
			"- Employee Report:\n"
			f"Employee: {employee.name},\n"
			f"Hours Worked: {employee.hours_worked},\n"
			f"Hourly Rate: {employee.hourly_rate}\n"
			f"Total Salary: {calculated_salary}\n"
		)

	def generate_annual_report(self, employee, calculated_salary) -> str:
		return (
			"- Employee Annual Report:\n"
			f"Employee: {employee.name},\n"
			f"Hours Worked: {employee.hours_worked},\n"
			f"Hourly Rate: {employee.hourly_rate}\n"
			f"Total Salary: {calculated_salary}\n"
		)

	def generate_bonus_report(self, employee, calculated_salary) -> str:
		return (
			"- Employee Bonus Report:\n"
			f"Employee: {employee.name},\n"
			f"Hours Worked: {employee.hours_worked},\n"
			f"Hourly Rate: {employee.hourly_rate}\n"
			f"Total Salary: {calculated_salary}\n"
		)