# Program to find GCD 

# Here magic happens
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def main():
	x = int(input("Enter a num: "))
	y = int(input("Enter another num: "))
	print("GCD = " + str(gcd(x, y)))


if __name__ == '__main__':
	main()