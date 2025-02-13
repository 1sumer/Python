from salary_calculator import SalaryCalculator

if __name__ == "__main__":
    # Manually input values
    base_salary = float(input("Enter base salary: "))
    leave_days = int(input("Enter number of leave days: "))
    target = float(input("Enter target: "))

    # Create an instance of SalaryCalculator
    salary_calculator = SalaryCalculator(base_salary)

    # Calculate net salary
    net_salary = salary_calculator.calculate_net_salary(leave_days, target)
    
    print(f"Net Salary: {net_salary}")