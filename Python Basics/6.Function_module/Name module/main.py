from greetings import calculator

obj = calculator(12, 14)

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Addition")
    print(obj.add())
else:
    print("Subtraction")
    print(obj.sub())

