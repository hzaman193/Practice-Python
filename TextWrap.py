def wrap_function(my_string, max_width):
    new_string = ""
    for i in range(0, len(my_string), max_width):
        new_string = new_string + my_string[i:max_width + i] + "\n"
    return new_string


string, m_width = input(), int(input())
result = wrap_function(string, m_width)
print(result)
