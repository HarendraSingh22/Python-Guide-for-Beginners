#uses python 3, tabulation technique
a, b= 0, 1
num_of_terms = input("Enter number of terms")
if num_of_terms>0:
    print("0")
for i in range(num_of_terms):
    c=a+b
    a, b = b, a
    print(c)
