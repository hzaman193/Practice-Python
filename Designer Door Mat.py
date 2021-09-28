i = 1
k = 1
while i <= 7:
    b = 1
    while b <= 7 - i:
        print(" ", end=" ")
        b = b + 1
    j = 1
    while j <= k:
        print("*", end=" ")
        j = j + 1
    k = k + 2
    print()
    i = i + 1
i = 7
k = 7
while i > 0:
    b = 1
    while b <= k-i:
        print(" ", end=" ")
        b = b + 1
    j = 1
    while j <= (i * 2) - 1:
        print("*", end=" ")
        j = j + 1
    print()
    i = i - 1
