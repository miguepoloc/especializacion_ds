from employee import Employee
from salary_calculator import SalaryCalculator
from report_generator import ReportGenerator

def main():
    employee = Employee("Jose Perez", 40, 25, 0.10)
    salary_calculator = SalaryCalculator()
    report_generator = ReportGenerator()
    bonnu_extra = 40

    calculated_salary_normal = salary_calculator.calculate_salary(employee)
    calculated_salary_annual = salary_calculator.calculate_annual_salary(employee)
    calculated_salary_bonus = salary_calculator.calculate_bonus(employee) + bonnu_extra


    print(report_generator.generate_report(employee=employee, calculated_salary=calculated_salary_normal))
    print(report_generator.generate_annual_report(employee=employee, calculated_salary=calculated_salary_annual))
    print(report_generator.generate_bonus_report(employee=employee, calculated_salary=calculated_salary_bonus))

main()
