import math

def num(num): #소수 구하는 함수
    if num == 1: # 소수구하는 조건1. 1은 소수가 아니다.
        return False
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num%i == 0:
                return False
        return True

all_list = list(range(2, 246912)) #문제에서 주어진 범위 // 이 범위를 정해두지 않으면 시간초과가 난다.
save_list = []

for i in all_list: #주어진 범위 안에서 소수들을 찾아 저장한다.
    if num(i):
        save_list.append(i)

num = int(input())

while num != 0:
    count = 0
    for i in save_list:
        if num < i <= num*2:
            count += 1
    print(count)
    num = int(input())