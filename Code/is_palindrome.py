def is_palindrome(num):
    s_num = str(num)
    return s_num == s_num[::-1]


num = int(input('Please enter a number: '))
print('{} is {}a palindrome.'.format(num, '' if is_palindrome(num) else 'not '))
