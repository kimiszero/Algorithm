import sys

n = int(input()) #입력받는 수의 개수 n
n_list = [0] * 10001 # 리스트크기 <= 10000
for i in range(n):
    n_list[int(sys.stdin.readline())] += 1
for i in range(10001):
    if n_list[i] != 0:
        for j in range(n_list[i]):
            print(i)