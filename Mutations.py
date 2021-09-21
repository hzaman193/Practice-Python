s = input()
i, c = input().split()
i = int(i)
# print(s[:i] + c + s[i + 1:])
my_list = list(s)
for index, item in enumerate(my_list):
    if index == i:
        my_list[i] = c
new_str = ""
for i in my_list:
    new_str = new_str + i
print(new_str)




