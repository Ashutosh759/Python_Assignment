#Write a function that accepts a string and returns the number of characters in it using if else.
def count_characters(s):
    return len(s)

s = input("Enter a string: ")
print(f"The number of characters in the string is: {count_characters(s)}")