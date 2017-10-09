"""Author : Harshad Reddy Nalla
    
    GCD (Greater Common Divisor) function in python
    This function will return the gcd between two number
"""
def GCD(x_value, y_value):
    while x_value != y_value:
        if x_value>y_value:
            x_value = x_value - y_value
        else:
            y_value = y_value - x_value 
    return x_value
    
if __name__ == "__main__":
    print "***Lets find GCD of 2 Numbers***"
    print "--------------------------------"
    x_value = input("Enter the first number value:")
    y_value = input("Enter the second number value:")
    print "\nThe greater common divisor of the two number", x_value, "and",y_value ,"is", GCD(x_value,y_value)