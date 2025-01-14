#Input a positive integer and count how many digits it has
Count digits of a number.
n = int(input("Enter the number: "))
count = 0
while n != 0:
    n //= 10
    count += 1
print("The number of digits in the number is: ", count)

    