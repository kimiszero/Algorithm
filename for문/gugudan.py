# 구구단
# N = int(input())
# if N >= 2 and N <= 9 :        
#     for i in range(1,10) :
#         print ('%d * %d = %d' %(N, i , N*i))
# else :
#     print('2부터 9까지 숫자를 입력하세요')

# A + B -3
# T = int(input())
# for i in range(1, T+1) :
#     A, B = map(int, input().split())
#     print(A + B)

# 합
# n = int(input())
# sum = 0
# if n >= 1 and n <= 10000 :
#     for i in(range(1, n+1)) :
#         sum += i
# print(sum)    

# 빠른 A+B
#import sys
# T =  int(input())
# if T <= 1000000 : 
#     for i in (range(1, T+1)) :
#         a,b = map(int, sys.stdin.readline().split())
#         print(a+b)

# N 찍기
# import sys

# N = int(sys.stdin.readline())
# if N <= 100000 :
#    for i in (range(1, N+1)) :
#        print(i)

# 기찍 N
# import sys
# N = int(sys.stdin.readline())
# if N <= 100000 :
#    for i in reversed(range (N)) :
#        print(i+1)

# A + B - 7
# import sys
# T = int(sys.stdin.readline())
# if T <= 10 :
#     for i in (range(1, T+1)) :
#         A,B = map(int, sys.stdin.readline().split())
#         print('Case #' , i , ': ' , A+B)

# A + B - 8
# import sys
# T = int(sys.stdin.readline())
# for i in (range(1, T+1)) :
#     A,B = map(int, sys.stdin.readline().split())
#     C = A + B
#     if A > 0 and B < 10 : 
#         print(f'Case #{i}: {A} + {B} = {C}')
#     else : 
#         print('A는 0보다 크고 B는 10보다 작아야 합니다.')

# 별 찍기 - 1
# import sys
# N = int(sys.stdin.readline())
# if N >= 1 and N <= 100 :
#     for i in (range (1, N+1)) :
#         print('*' * i)

# 별 찍기 - 2
# import sys
# N = int(sys.stdin.readline())
# if N >= 1 and N <= 100 :
#     for i in (range (1, N+1)) :
#         print(str('*' * i).rjust(N))

# X보다 작은 수
import sys
N,X = map(int, sys.stdin.readline().split())
if(N,X >=1 and N,X <= 10000) :
    A = list(map(int, sys.stdin.readline().split()[:N]))
    print(A)
    for i in A : 
        if i < X :
            print(i, end=' ')
