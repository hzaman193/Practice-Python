def split_and_join(line):
    str_my = line.split(" ")
    str_my = "-".join(str_my)
    return str_my
nn = "tthis is a string"
print(split_and_join(nn))
