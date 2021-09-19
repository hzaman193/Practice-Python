n = int(input())
score_list = list(map(int, input().split()))[:n]
t = tuple(score_list)
print(hash(t))
# from past.builtins import raw_input, xrange
# n = raw_input()
# input_line = raw_input()
# input_list = input_line.split()
# input_list = map(int, input_list)
# t = tuple(input_list)
# print(hash(t))


