# Find the first non-repeating character

text = input("Enter the text: ")

def first_non_repeating_char(text):
    freq = {}

    for char in text:
        freq[char] = freq.get(char, 0) + 1

    for char in text:
        if freq[char] == 1:
            return char

    return None

print(first_non_repeating_char(text))

