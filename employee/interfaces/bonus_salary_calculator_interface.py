from abc import ABC, abstractmethod

class IBonusSalaryCalculator(ABC):
    @abstractmethod
    def calculate_salary_with_bonus(self, employee):
        pass