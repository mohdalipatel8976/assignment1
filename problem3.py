rows = int(input("Enter the number of rows for the pyramid: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
