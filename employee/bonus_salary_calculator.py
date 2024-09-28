from salary_calculator import SalaryCalculator

class BonusSalaryCalculator(SalaryCalculator):
    def __init__(self, bonus_rate):
        self.bonus_rate = bonus_rate

    def calculate_salary_with_bonus(self, employee):
        base_salary = super().calculate_salary(employee)
        return base_salary + (base_salary * self.bonus_rate)
