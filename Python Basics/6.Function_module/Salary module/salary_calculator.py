from base_salary import BaseSalary
from deduction import Deduction
from incentive import Incentive

class SalaryCalculator:
    def __init__(self, base_salary):
        self.base_salary_obj = BaseSalary(base_salary)

    def calculate_net_salary(self, leave_days, target):
        base_salary = self.base_salary_obj.get_base_salary()
        
        deduction_obj = Deduction(base_salary)
        deduction_amount = deduction_obj.calculate_deduction(leave_days)
        
        incentive_obj = Incentive(base_salary)
        incentive_amount = incentive_obj.calculate_incentive(target)

        net_salary = base_salary - deduction_amount + incentive_amount
        return net_salary