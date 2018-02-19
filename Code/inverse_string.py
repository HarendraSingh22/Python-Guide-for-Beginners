#Taking input from users
string = input("Select a string to invert")

#Create a string to hold the string that is going to be built
final_string = ""

#Loop trough the string starting from the lenght of the string to 0 reducing 1 each time
for i in range(len(string)-1,-1,-1):
    
    final_string += string[i]

#Display the result
print(final_string)
