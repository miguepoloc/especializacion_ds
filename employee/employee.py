class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self._name         = name
        self._hours_worked = hours_worked
        self._hourly_rate  = hourly_rate

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def hours_worked(self):
        return self._hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        self._hours_worked = value

    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        self._hourly_rate = value

    def calculate_salary(self):
        return self._hours_worked * self._hourly_rate

    def generate_report(self):
        return f"Employee: {self._name}, Hours Worked: {self._hours_worked}, Hourly Rate: {self._hourly_rate}"
