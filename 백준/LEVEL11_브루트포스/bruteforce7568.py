#덩치 순위구하는 알고리즘
n = int(input()) #첫번째입력 : 전체 사람의 수
sum_list = [] #입력받은 순서대로 몸무게와 키를 더해서 저장할 리스트
rank_list = [] #등수정보를 저장할 리스트

for i in range(n):
  sum_list.append(list(map(int, input().split()))) #두번째 입력 : 각 사람의 몸무게와 키

for i in range(n):
    rank = 1
    for j in range(n):
        if sum_list[i][0] < sum_list[j][0] and sum_list[i][1] < sum_list[j][1]:
            rank += 1
    rank_list.append(rank)

for i in rank_list:
    print(i, end=' ')