import math

def isPrime(n):#소수 구하는 함수
    if n == 1: #소수 조건1. 1은 소수가 아니다.
        return False 
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

all_list = list(range(2, 246912)) #문제에서 지정해준 범위
prime_list = [] #소수의 범위
for i in all_list: #모든 범위 안에서 반복문을 돌린다. 
    if isPrime(i):
        prime_list.append(i)

n = int(input()) #입력받은 정수 n

while n != 0: #0이 입력되면 종료한다. 
    count = 0 #소수의 개수
    for i in prime_list:
        if n < i <= n*2:
            count +=1
    print(count)
    n = int(input()) #0이 입력될 때까지 새로운 n을 입력받는다.