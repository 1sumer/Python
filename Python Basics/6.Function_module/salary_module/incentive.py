class Incentive:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_incentive(self, sales_amount, target=2000):
        if sales_amount >= target:
            incentive = 0.005 * self.base_salary
        else:
            incentive = 0
        return incentive
