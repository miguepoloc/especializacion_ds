from employee import Employee

class ReportGenerator:
	def generate_report(self, employee):
		return (
			"- Employee Report: "
			f"Employee: {employee.name},"
			f"Hours Worked: {employee.hours_worked},"
			f"Hourly Rate: {employee.hourly_rate}\n"
		)