n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    score = list(map(float, line))
    student_marks[name] = score
query_name = input()
#print(student_marks.values())
sum_score = 0
value_score = 0
for key, value in student_marks.items():
    if key == query_name:
        for i in value:
            sum_score = (sum_score + i)
        value_score = sum_score/len(value)
print('{0:.2f}'.format(value_score))
