def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    return fib_series[:n]

# Get user input
num_terms = int(input("Enter the number of terms: "))

# Generate and print Fibonacci series
print("Fibonacci Series:", fibonacci(num_terms))

