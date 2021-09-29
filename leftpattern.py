n = int(input())
for i in range(0, n):
    b = 1
    while b < n - i:
        print(" ", end=" ")
        b = b + 1
    for j in range(i + 1):
        print("*", end=" ")
    print()
for i in range(n+1):
    b = 1
    while b <= n-i:
        print(" ", end=" ")
        b = b + 1
    for j in range(i - 1):
        print("*", end=" ")
    print()


