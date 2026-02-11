# Check if string is a palindrome

def is_palindrome(s):
    return s == s[::-1]

str = input("Enter any word: ")
print("The given string ",str, is_palindrome(str))
