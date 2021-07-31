import sys

N = int(input())
new_list = []

score_list = list(map(int, input().split()))
max_score = max(score_list)

for i in score_list : 
    new_list.append(i/max_score * 100)
score_avg = sum(new_list)/N
print(score_avg)