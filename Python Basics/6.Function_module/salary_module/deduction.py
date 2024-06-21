class Deduction:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_deduction(self, leave_days):
        daily_salary = self.base_salary / 30
        deduction = daily_salary * leave_days
        return deduction