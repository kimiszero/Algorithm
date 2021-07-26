import sys

N = int(sys.stdin.readline())
count = 0 #N의 사이클 길이
result = 0 #수행한 연산값
new_N = 0 #새로 만들어질 N값 

while True :
    if N >= 0 and N <= 99 :
        A = N // 10
        B = N % 10
        result = A + B
        count = count + 1
        new_N = (N % 10) * 10 +  result % 10
        if new_N != N :
            print(result + B)
        else :
            print(count)
            break