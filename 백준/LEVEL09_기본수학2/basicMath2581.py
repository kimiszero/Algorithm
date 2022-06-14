M = int(input())
N = int(input())
prime = [] # 최소값을 구하기 위한 소수 리스트

for i in range(M, N+1):
    cnt = 0
    if i > 1 :
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
                break
        if cnt == 0 :
            prime.append(i)

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
