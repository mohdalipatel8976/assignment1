rows = int(input("Enter the number of rows for the triangle: "))

for i in range(1, rows + 1):
    for j in range(rows - i + 1):
        print(i, end=" ")
    print()
