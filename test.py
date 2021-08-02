C = int(input())

for i in range(C) :
    try:
        N = list(map(int, input().split()))
    except :
        print('입력되지 않았습니다')
    else :
        avg = sum(N[1:]) / N[0]
        cnt = 0 
        for j in N[1:] :
            if j > avg :
                cnt += 1
        print(str('%.3f' %round((cnt/N[0])*100, 3))+ '%')