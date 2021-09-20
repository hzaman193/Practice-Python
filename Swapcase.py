def swap_case(s):
    new_string = ""
    for i in s:
        o = ord(i)
        if o in range(65, 91):
            new_string = new_string + i.lower()
        # elif o in range(97, 123):
        #     new_string = new_string + i.upper()
        else:
            new_string = new_string + i.upper()
    return new_string

swap_string = input()
result = swap_case(swap_string)
print(result)
