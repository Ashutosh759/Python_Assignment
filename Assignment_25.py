#Write a function fibonacci(n) that returns a list of the first n Fibonacci numbers.

Fibonacci Series (Function)
def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(f"The first {n} Fibonacci numbers are: {fibonacci(n)}")