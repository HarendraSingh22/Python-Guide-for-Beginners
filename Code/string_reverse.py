# Given a string, return a new string where the first and last chars have been exchanged.


# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(given_string):
	new_str = ''
	for index in range(len(given_string),0,-1):
		
		new_str += given_string[index-1]
		
	return new_str
	
str_reverse = front_back('code')
print(str_reverse)