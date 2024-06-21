from base_salary import BaseSalary
from deduction import Deduction
from incentive import Incentive

class SalaryCalculator:
    def __init__(self, base_salary):
        self.base_salary_obj = BaseSalary(base_salary)

    def calculate_net_salary(self, leave_days, sales_amount):
        base_salary = self.base_salary_obj.get_base_salary()
        
        deduction_amount = Deduction.calculate_deduction(base_salary, leave_days)
        incentive_amount = Incentive.calculate_incentive(base_salary, sales_amount)

        net_salary = base_salary - deduction_amount + incentive_amount
        return net_salary

# Example usage
if __name__ == "__main__":
    # Manually input values
    base_salary = float(input("Enter base salary: "))
    leave_days = int(input("Enter number of leave days: "))
    sales_amount = float(input("Enter sales amount: "))

    # Create an instance of SalaryCalculator
    salary_calculator = SalaryCalculator(base_salary)

    # Calculate net salary
    net_salary = salary_calculator.calculate_net_salary(leave_days, sales_amount)
    
    print(f"Net Salary: {net_salary}")
