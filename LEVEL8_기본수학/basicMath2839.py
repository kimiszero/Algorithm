N = int(input()) # 배달해야하는 설탕의 킬로그램

if N % 5 == 0 :
    print(N // 5)
elif N % 5 == 3 :
    print(N // 5 + 1)
elif N % 3 == 0 :
    print(N // 3)
elif N % 3 == 2 :
    print(N // 3)
else :
    print(-1)
