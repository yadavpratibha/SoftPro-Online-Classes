def generate_fibonacci(n):
    fib_series = []
    a=0
    b=1
    for i in range(n):
        fib_series.append(a)
        a=b
        b=a+b
    return fib_series

n = int(input("Enter the number of terms: "))
fibonacci = generate_fibonacci(n)
print(fibonacci)
