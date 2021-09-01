import math

#n이하의 숫자 중 소수 찾기
def isPrime(n):
    sieve = [True] * n
    m = int(math.sqrt(n))
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

#n이하의 소수들 중 합이 n
def sosu(n):
    li=isPrime(n)
    idx = max([i for i in range(len(li)) if li[i]<=n/2])
    for i in range(idx, -1, -1):
        for j in range(i, len(li)):
            if li[i]+li[j] == n:
                return [li[i], li[j]]

T = int(input()) #테스트 케이스의 개수 n

for i in range(T+1):
    n = int(input()) #입력되는 짝수 n
    print(' '.join(map(str, sosu(n))))