import math

#소수를 구하는 함수
def isPrime(num):
    if num == 1: #소수구하는 조건1: 1은 소수가 아니다.
        return False
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True

all_list = list(range(2, 246912)) #문제에서 주어진 범위
save_list = []

for i in all_list: #주어진 범위 내에서 소수들을 찾아 저장한다. 
    if isPrime(i):
        save_list.append(i)

num = int(input()) #입력받은 정수 n

while num != 0 : #n이 0이 입력되면 종료한다. 
    count = 0 #소수의 개수
    for i in save_list:
        if num < i <= num*2:
            count += 1
    print(count)
    num = int(input()) #0이 입력될 때까지 새로운 n을 입력받는다.