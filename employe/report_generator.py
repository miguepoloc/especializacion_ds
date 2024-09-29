from employee import Employee

class ReportGenerator:
    def generate_report(self, employee, calculated_type="normal", calculated_salary=None):
        report_switch = {
            "normal": lambda: (
                "- Employee Report:\n"
                f"Employee: {employee.name},\n"
                f"Hours Worked: {employee.hours_worked},\n"
                f"Hourly Rate: {employee.hourly_rate}\n"
                f"Total Salary: {calculated_salary}\n"
            ),
            "annual": lambda: (
                "- Detailed Employee Report:\n"
                f"Employee: {employee.name}\n"
                f"Total Hours Worked: {employee.hours_worked}\n"
                f"Hourly Rate: {employee.hourly_rate}\n"
                f"Annual Salary: {calculated_salary}\n"
            ),
            "Bonnus": lambda: (
                "- Bonnus Employee Report:\n"
                f"Employee: {employee.name}\n"
                f"Total Hours Worked: {employee.hours_worked}\n"
                f"Hourly Rate: {employee.hourly_rate}\n"
                f"Total Salary with Bonus: {calculated_salary}\n"
            )
        }

        report_function = report_switch.get(calculated_type, report_switch["normal"])

        return report_function()