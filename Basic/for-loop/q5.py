# Print the factorial of a number

factorial = 1

try:
     user_input = input("Enter a number: ")
     num = int(user_input)
except ValueError:
    print("Invalid input. Please enter a whole number for age.")

for i in range(num , 0, -1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")