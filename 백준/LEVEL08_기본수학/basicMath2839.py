N = int(input()) # 배달해야하는 설탕의 킬로그램
cnt = 0 # 배달의 수

while N >= 0 :
    if (N % 5) == 0 :
        cnt += (N // 5)
        print(cnt)
        break
    N -= 3
    cnt += 1
else :
    print('-1')