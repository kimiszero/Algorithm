import math

# 소수인지 검사해주는 함수
def isPrime(num):
    if num == 1: 
        return False
    else:    
        for i in range(2, int(math.sqrt(num))+1):  
            if num % i == 0: 
                return False
        return True

M, N = map(int, input().split()) #자연수 M이상 N이하의 소수를 구한다. 

for i in range(M, N+1):
    if isPrime(i):
        print(i)