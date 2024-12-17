n_terms = int(input("Enter the number of terms for the Fibonacci series: "))

a, b = 0, 1
print("Fibonacci Series:", end=" ")


for _ in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b
print()
