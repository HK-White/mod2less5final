def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("You can't divide by zero, goober! Try again if you wish.")
        return None
    return a / b

def calculation():
    while True:
        print("Which operation are we doing?")
        print("1. for Addition +")
        print("2. for Subtraction -")
        print("3. for Multiplication *")
        print("4. for Division")
        print("5. Cancel Operation")

        option = input("Enter operator selection(1/2/3/4/5): ")

        if option == '5':
            print("Operation Stopped. Good bye!")
            break
        
        if option in ('1', '2', '3', '4'):
            number1 = float(input("First Number: "))
            number2 = float(input("Second Number: "))

            if option == '1':
                print(f"Result: {add(number1, number2)}")
            elif option == '2':
                print(f"Result: {subtract(number1, number2)}")
            elif option == '3':
                print(f"Result: {multiply(number1, number2)}")
            elif option == '4':
                print(f"Result: {divide(number1, number2)}")
            break
        else:
            print("Error! Maybe you entered an invalid selection. Please try again.")


calculation()

# This is a basic caluculator made with functions as the assignment
# calls for. Not made with AI, just from using the official python
# documentation :-)
