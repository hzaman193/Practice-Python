n = int(input())
status = ""
if n % 2 == 1 or n % 2 == 0 and n in range(6, 21):
    status = "Weird"
elif n in range(2,6) and n > 20 and  n % 2 == 0:
    status = "Not Weird"
else:
    status = "Not Weird"
print(status)



