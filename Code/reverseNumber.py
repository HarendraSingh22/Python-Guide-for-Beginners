#reversing a given number in python
#Sample Input: 123 
#Sample Output:321

def revNum(n):
    rev = 0
    while(n>0):
        dig = n%10
        rev=rev*10+dig
        n=n//10
    return rev
   
   
n=int(input("Enter number: "))
rev = revNum(n)
print("Reverse of the number:",rev)
   
   
