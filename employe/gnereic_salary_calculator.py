from abc import ABC, abstractmethod

class GenericSalaryCalculator(ABC):
	@abstractmethod
	def calculate_salary(self, employee) -> float:
		pass

	@abstractmethod
	def calculate_annual_salary(self, employee) -> float:
		pass

	@abstractmethod
	def calculate_bonus(self, employee) -> float:
		pass