''' Return true if x is a palindrome, and false otherwise.'''

def is_palindrome(x):
    return(str(x) == str(x)[::-1])
print(is_palindrome(-121))
