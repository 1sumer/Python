from base_salary import BaseSalary
from deduction import Deduction
from incentive import Incentive

class SalaryCalculator:
    def __init__(self, base_salary):
        self.base_salary_obj = BaseSalary(base_salary)
        self.deduction_obj = Deduction(base_salary)
        self.incentive_obj = Incentive(base_salary)

    def calculate_net_salary(self, leave_days, target):
        base_salary = self.base_salary_obj.get_base_salary()
        deduction_amount = self.deduction_obj.calculate_deduction(leave_days)
        incentive_amount = self.incentive_obj.calculate_incentive(target)
        net_salary = base_salary - deduction_amount + incentive_amount
        return net_salary