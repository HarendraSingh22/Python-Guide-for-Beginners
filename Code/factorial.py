
#program to find the factorial of a number provided by a user

if __name__ == "__main__":
    number = int(raw_input("Enter a number to get its factorial: "))
    factorial = 1

    if number < 0:
        print("Sorry, factorial doesn't exist for negative numbers!")
    elif number == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, number + 1):
            factorial = factorial * i
        print "The factorial of %r is %r" % (number, factorial)
    