N = int(input())
num = list(map(int, input().split()))[:N]
prime_cnt = 0 # 소수의 개수

for i in num:
    cnt = 0 # 나머지가 0의 수
    if i > 1 :
        for j in range(2, i) :
            if i % j == 0 :
                cnt += 1
        if cnt == 0 :
            prime_cnt += 1
print(prime_cnt)