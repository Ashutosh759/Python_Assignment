#Input a positive integer and reverse its digits (e.g., 123 -> 321)
Reverse a number.(While loop)
n = int(input("Enter the number: "))
rev = 0
while n != 0:
    rev = rev*10 + n%10
    n //= 10
print("The reversed number is: ", rev)
    