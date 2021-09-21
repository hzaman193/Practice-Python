def count_sub_string(my_string, my_sub_string):
    total_count = (1 for i in range(len(my_string)) if my_string.startswith(my_sub_string, i))
    return total_count
    # count = 0
    # for i in range(len(my_string)):
    #     if my_string[i:].startswith(my_sub_string):
    #         count = count + 1
    # return count


string_new = input()
sub_string = input()
result = count_sub_string(string_new, sub_string)
print(result)
