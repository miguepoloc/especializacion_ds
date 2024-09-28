from abc import ABC, abstractmethod

class IBonusEmployeeReport(ABC):
    @abstractmethod
    def generate_detailed_report_with_bonus(self, employee, salary_calculator):
        pass
