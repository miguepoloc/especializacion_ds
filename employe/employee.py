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

    def update_hours_worked(self, additional_hours):
        self.__hours_worked += additional_hours

    def update_hourly_rate(self, new_rate):
        self.__hourly_rate = new_rate

    def calculate_salary(self):
        return self.__hours_worked * self.__hourly_rate

    def calculate_annual_salary(self):
        return self.calculate_salary() * 52

    def calculate_salary_with_bonus(self):
        base_salary = self.calculate_salary()
        return base_salary + (base_salary * self.__bonus_rate)

    def generate_report(self):
        return (
            "- Employee Report: "
            f"Employee: {self.__name},"
            f"Hours Worked: {self.__hours_worked},"
            f"Hourly Rate: {self.__hourly_rate}\n"
        )

    def generate_detailed_report(self):
        monthly_salary = self.calculate_salary()
        annual_salary = self.calculate_annual_salary()
        return (
            "- Detailed Employee Report: \n"
            f"Employee: {self.__name}\n"
            f"Hours Worked: {self.__hours_worked}\n"
            f"Hourly Rate: {self.__hourly_rate}\n"
            f"Monthly Salary: {monthly_salary}\n"
            f"Annual Salary: {annual_salary}\n"
        )

    def generate_detailed_report_with_bonus(self):
        monthly_salary_with_bonus = self.calculate_salary_with_bonus()
        annual_salary_with_bonus = monthly_salary_with_bonus * 12
        return (
            "- Detailed Report With Bonus: \n"
            f"Employee: {self.__name}\n"
            f"Hours Worked: {self.__hours_worked}\n"
            f"Hourly Rate: {self.__hourly_rate}\n"
            f"Monthly Salary with Bonus: {monthly_salary_with_bonus}\n"
            f"Annual Salary with Bonus: {annual_salary_with_bonus}\n"
        )
