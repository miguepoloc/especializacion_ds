from abc import ABC, abstractmethod

class ISalaryCalculator(ABC):
    @abstractmethod
    def calculate_salary(self, employee):
        pass

    @abstractmethod
    def calculate_annual_salary(self, employee):
        pass
