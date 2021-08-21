T = int(input())
for i in range(T) :
    # H: 호텔 층수 W: 각 층의 방수 N: 몇번째 손님
    H, W, N = map(int, input().split())
    if N % H == 0 :
        F = H * 100
        room = N // H
    else :
        F = (N % H) * 100
        room = 1 + N // H
    print(F + room)    