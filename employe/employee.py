class Employee:
	def __init__(self, name, hours_worked, hourly_rate, bonus_rate):
		self.__name         = name
		self.__hours_worked = hours_worked
		self.__hourly_rate  = hourly_rate
		self.__bonus_rate   = bonus_rate

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		self.__name = value

	@property
	def hours_worked(self):
		return self.__hours_worked

	@hours_worked.setter
	def hours_worked(self, value):
		self.__hours_worked = value

	@property
	def hourly_rate(self):
		return self.__hourly_rate

	@hourly_rate.setter
	def hourly_rate(self, value):
		self.__hourly_rate = value

	@property
	def bonus_rate(self):
		return self.__bonus_rate

	@bonus_rate.setter
	def bonus_rate(self, value):
		self.__bonus_rate = value
