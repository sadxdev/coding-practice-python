# Print the factorial of a number

factorial = 1

num = int(input("enter the number: "))

for i in range(num, 0, -1):
    factorial *= i

print("The factorial of", num,"is", factorial)