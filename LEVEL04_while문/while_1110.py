import sys

N = int(sys.stdin.readline())
old_N = N #원래 N값
count = 0 #N의 사이클 길이
result = 0 #수행한 연산값
new_N = 0 #새로 만들어질 N값 

while True :
    if N >= 0 and N <= 99 :
        result = N // 10 + N % 10
        new_N = (N % 10) * 10 +  result % 10
        count = count + 1 
        N = new_N
        if old_N == new_N :
            break
print(count)