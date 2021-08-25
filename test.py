N = int(input())
num = list(map(int, input().split()))[:N]
prime_num = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 59, 61, 67, 71, 73, 77, 79, 83, 89, 91, 97]
cnt = 0 # 소수의 개수
for i in num:
    for j in prime_num:
        if i == j:
            cnt += 1
print(cnt)