import calculator
print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

choice = input("Enter your choice (1/2/3/4): ")

if choice == '1':
    print("Result:", calculator.add(num1, num2))
    
elif choice == '2':
    print("Result:", calculator.subtract(num1, num2))

elif choice == '3':
    print("Result:", calculator.multiply(num1, num2))
    
elif choice == '4':
    print("Result:", calculator.divide(num1, num2)) 
else:
    print("Invalid choice")