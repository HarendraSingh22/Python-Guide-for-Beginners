# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers


def subtract(x, y):
    return x - y

# This function multiplies two numbers


def multiply(x, y):
    return x * y

# This function divides two numbers


def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user
while True:

    try:
        print("(enter 'q' to quit anytime.)")
        choice = input("Enter choice(1/2/3/4):")
        if choice == 'q':
            break

        num1 = input("Enter first number: ")
        if num1 == 'q':
            break
        else:
            num1 = int(num1)

        num2 = input("Enter second number: ")
        if num2 == 'q':
            break
        else:
            num2 = int(num2)

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        else:
            print("Invalid Input")

    except ValueError:
        print("Invalid Input")
