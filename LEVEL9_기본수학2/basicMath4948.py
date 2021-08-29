import sys
import math

data = []

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        data.append(n)

# 입력 n의 범위는 1 <= n <= 123456 이므로, 2n의 값까지 y를 설정
y = 123456 * 2
arr = [True for _ in range(y+1)]
arr[1] = False

for i in range(2, int(math.sqrt(y))+1):
    if arr[i]:
        j = 2
        while i * j <= y:
            arr[i*j] = False
            j += 1


for x in data:
    count = 0 # data의 각 값들에 대한 count 초기화

    for i in range(x+1, 2*x+1): # x초과 2x이하까지 i가 돈다
        if arr[i]: # arr[i]가 True면 (소수이면)
            count += 1 # 카운트에 1 추가

print(count)