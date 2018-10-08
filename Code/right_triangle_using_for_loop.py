'''
To print a right triangle Using loops: 
https://goo.gl/PEyS9a
'''

def rtTriangle(n):
    '''
    objective : To print a right triangle 
    approach : Using loops
    '''
    for row in range(0,n):
        for column in range(0,row+1):
            print('*',end='')
        print('')
    
def main():
    '''
    objective : To print a right triangle 
    approach : Using print statements
    '''
    n=int(input("Enter number of rows : "))
    rtTriangle(n)
    
if __name__ == "__main__":
    main()
    
