# Find the most frequent character in a string

text = input("Enter the text: ")

def most_freq_char(text):
    freq = {}

    for char in text:
        freq[char] = freq.get(char, 0) + 1

    max_count = max(freq, key=freq.get)
    return max_count

print(most_freq_char(text))

