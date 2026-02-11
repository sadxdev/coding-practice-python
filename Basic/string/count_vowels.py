# Count vowels and consonants in a string

def count_vowels_consonants(text):
    vowels="aeiouAEIOU"
    v_count = 0
    c_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1

    return v_count, c_count

text = input("enter the text: ")

vowels, consonants = count_vowels_consonants(text)

print("Vowels: ", vowels)
print("Consonants: ", consonants)