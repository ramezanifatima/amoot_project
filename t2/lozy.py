num = int(input('enter number:'))
for i in range(num // 2 + 1):
    for j in range(num // 2 - i):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()

for i in range(num // 2 - 1, -1, -1):
        for j in range(num // 2 - i):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()