N, M = map(int, input().split())
for i in range(1, N, 2):
    print((str('.|.') * i).center(M, "-"))
print("WELCOME".center(M, "-"))
for i in range(N - 2, -1, -2):
    print((str('.|.') * i).center(M, "-"))



# N, M = map(int, input().split())
# for i in range(1, N, 2):
#     print((str('*') * i).center(M, " "))
# #print(("WELCOME").center(M, "-"))
# for i in range(N - 2, -1, -2):
#     print((str('*') * i).center(M, " "))
# i = 1
# k = 1
# while i <= 7:
#     b = 1
#     while b <= 7 - i:
#         print(" ", end=" ")
#         b = b + 1
#     j = 1
#     while j <= k:
#         print("*", end=" ")
#         j = j + 1
#     k = k + 2
#     print()
#     i = i + 1
# i = 7
# k = 7
# while i > 0:
#     b = 1
#     while b <= k-i:
#         print(" ", end=" ")
#         b = b + 1
#     j = 1
#     while j <= (i * 2) - 1:
#         print("*", end=" ")
#         j = j + 1
#     print()
#     i = i - 1
