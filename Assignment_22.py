#Write a function power(base, exponent) that returns base^exponent without using the built-in ** operator (use a loop)
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

# Calculate the power
result = 1
for i in range(exponent):
    result *= base

# Print the result
print(f"{base} raised to the power of {exponent} is: {result}")