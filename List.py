my_list = []
n = int(input())
for i in range(0, n):
    cmd = list(input().split())
    if cmd[0] == "insert":
        my_list.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == "insert":
        my_list.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == "insert":
        my_list.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == "print":
        print(my_list)
    elif cmd[0] == "remove":
        my_list.remove(int(cmd[1]))
    elif cmd[0] == "append":
        my_list.append(int(cmd[1]))
    elif cmd[0] == "append":
        my_list.append(int(cmd[1]))
    elif cmd[0] == "sort":
        my_list.sort()
    elif cmd[0] == "print":
        print(my_list)
    elif cmd[0] == "pop":
        my_list.pop()
    elif cmd[0] == "reverse":
        my_list.reverse()
    elif cmd[0] == "print":
        print(my_list)

