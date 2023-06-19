def fibonacci(n):
    fib = [0, 1]  # Initialize the first two Fibonacci numbers as a list
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])  # Add the sum of the last two numbers to the list
    return fib[n]  # Return the desired Fibonacci number

# Ask the user for a number to calculate the Fibonacci series
number = int(input("Enter the position of the Fibonacci number you want to calculate: "))

# Calculate the Fibonacci number requested by the user and print it to the screen
result = fibonacci(number)
print(f"The {number}th Fibonacci number is: {result}")
