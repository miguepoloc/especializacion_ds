from abc import ABC, abstractmethod

class IReport(ABC):
    @abstractmethod
    def generate_report(self, employee, calculated_salary) -> str:
        pass

    @abstractmethod
    def generate_annual_report(self, employee, calculated_salary) -> str:
        pass

    @abstractmethod
    def generate_bonus_report(self, employee, calculated_salary) -> str:
        pass