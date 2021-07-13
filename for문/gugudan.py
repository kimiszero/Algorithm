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
n = int(input())
sum = 0
if n >= 1 and n <= 10000 :
    for i in(range(1, n+1)) :
        sum += i
print(sum)    