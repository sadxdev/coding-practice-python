# Check if string is a palindrome

text = input("Enter the text: ")

def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome(text))