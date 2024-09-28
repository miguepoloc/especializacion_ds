from abc import ABC, abstractmethod

class IEmployeeReport(ABC):
    @abstractmethod
    def generate_report(self, employee):
        pass

    @abstractmethod
    def generate_detailed_report(self, employee, salary_calculator):
        pass
