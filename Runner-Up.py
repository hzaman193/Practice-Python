n = int(input())
score_list = list(map(int, input().strip().split()))[:n]
temp = 0
for i in range(n):
    for j in range(n-1-i):
        if(score_list[j] > score_list[j+1]):
            temp = score_list[j]
            score_list[j] = score_list[j + 1]
            score_list[j + 1] = temp

res = []
[res.append(x) for x in score_list if x not in res]
print(res)
print(res[len(res) - 2])


