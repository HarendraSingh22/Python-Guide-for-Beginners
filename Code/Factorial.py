
#program to find the factorial of a number provided by a user

def fact(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    return factorial

if __name__ == "__main__":
    number = int(input("Enter a number to get its factorial: "))
    if number < 0:
        print("Sorry, factorial doesn't exist for negative numbers!")
    result = fact(number)
    print("factorial of",number,"is :",result)
