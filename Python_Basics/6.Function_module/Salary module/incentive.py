class Incentive:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_incentive(self, target, sales_amount=2000):
        if target >= sales_amount:
            incentive = 0.005 * self.base_salary
        else:
            incentive = 0
        return incentive