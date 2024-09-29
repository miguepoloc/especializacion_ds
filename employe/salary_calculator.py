class SalaryCalculator:
    def calculate_salary(self, employee, calculated_type="normal"):
        calculation_switch = {
            "normal": lambda: employee.hours_worked * employee.hourly_rate,
            "annual": lambda: employee.hours_worked * employee.hourly_rate * 30,
            "bonus": lambda: employee.hours_worked * employee.hourly_rate * (1 + employee.bonus_rate)
        }

        calculate_function = calculation_switch.get(calculated_type, calculation_switch["normal"])

        return calculate_function()
