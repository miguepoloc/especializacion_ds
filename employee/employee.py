class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.__name = name
        self.__hours_worked = hours_worked
        self.__hourly_rate = hourly_rate

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