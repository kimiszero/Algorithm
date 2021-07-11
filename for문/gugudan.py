# 구구단
N = int(input())
if N >= 2 and N <= 9 :        
    for i in range(1,10) :
        print ('%d * %d = %d' %(N, i , N*i))
else :
    print('2부터 9까지 숫자를 입력하세요')
