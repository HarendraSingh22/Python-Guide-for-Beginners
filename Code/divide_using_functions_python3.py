def inputOne():
    numOne = input("Enter first number: ")
    return numOne

def inputTwo():
    numTwo = input("Enter second number: ")
    return numTwo

def divideFunction(numOne, numTwo):
    Division = float(numOne)/float(numTwo)
    print("Result = "+ str(Division))

def mainFunction():
    numOne = inputOne()
    numTwo = inputTwo()
    if numTwo=='0':
        print('Denominator cannot be 0, Please Try Again') 
        mainFunction()

    else:
        divideFunction(numOne, numTwo)

mainFunction()
