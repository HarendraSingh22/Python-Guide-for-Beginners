import math

def degreeToRadians(xDegrees):
    '''
    Objective    : To convert the given degrees to Radians
    parameters   :
        xDegrees : integer - Degree of angle whose radians is to be calculated
    return value :
        xRadians : integer - The converted value of Degrees to Radians
    '''
    #approach : Using the formula, radians = degree * (pi/180)

    xRadians= xDegrees*(math.pi/180) 
    return xRadians


def cosine(xDegrees):
    '''
    Objective    : To find the value of cosine(x)
    parameters   :
        xDegrees : integer - Degree of angle whose cosine is to be calculated
    return value :
          total  : integer - The converted value of Degrees to Radians
    
    '''
    # approach     : Convert the given x degrees to radians using the function degreeToRadians(x),
    #                then punch the value of radians into the Maclaurin series
    
    xRadians=degreeToRadians(xDegrees)

    epsilon=0.00001

    total=1
    term = 1
    nextTerm=1
    multiplyBy = -xRadians*xRadians

    while abs(term) > epsilon :
        divideBy   = nextTerm*(nextTerm+1)
        term       = term*multiplyBy/divideBy
        total     += term
        nextTerm  += 2

    return total


def sine(xDegrees):
    '''
    Objective    : To find the value of sine(x)
    parameters   :
        xDegrees : integer - Degree of angle whose sine is to be calculated
    return value :
          total  : integer - The converted value of Degrees to Radians
    
    '''
    # approach     : Convert the given x degrees to radians using the function degreeToRadians(x),
    #                then punch the value of radians into the Maclaurin series
    
    xRadians=degreeToRadians(xDegrees)

    epsilon=0.00001

    total=xRadians
    term = xRadians
    nextTerm=2
    multiplyBy = -xRadians*xRadians

    while abs(term) > epsilon :
        divideBy   = nextTerm*(nextTerm+1)
        term       = term*multiplyBy/divideBy
        total     += term
        nextTerm  += 2

    return total


def main():
    '''
    Objective   : To print the value cosine x
    User inputs :
         x - int : The value in degrees whose cosine is to be calculated
         
    '''
    #approach : Using Taylor series expansion of cosine x
    print('{:^40}'.format("Trigonometric functions"))
    
    print("\n \
          1. Sine x  \n \
          2. Cosine x \n")

    choice = int(input("Enter your choice:  "))
    print("")

    if choice == 1:
       xDegrees = int(input("Enter the angle in degrees :  "))
       print('Value of  Sine',xDegrees,'is       : ', sine(xDegrees))

    elif choice == 2:
       xDegrees = int(input("Enter the angle in degrees :  "))
       print('Value of Cosine',xDegrees,'is      : ', cosine(xDegrees))

    else:
          print("Invalid Option. Retry !")
       
if __name__ == '__main__':
     main()
     print("\nEnd of the Program\n")
