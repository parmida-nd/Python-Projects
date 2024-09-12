# Simple calculator in Python 
def calculator():
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator.")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice, please select a valid operation.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == '1':
            print("%f + %f = %f" % (num1, num2, num1 + num2))
        elif choice == '2':
            print("%f - %f = %f" % (num1, num2, num1 - num2))
        elif choice == '3':
            print("%f * %f = %f" % (num1, num2, num1 * num2))
        elif choice == '4':
            if num2 != 0:
                print("%f / %f = %f" % (num1, num2, num1 / num2))
            else:
                print("Error! Division by zero.")

# Run the calculator
calculator()
