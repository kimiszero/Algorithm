T = int(input())

for i in range(3) :
    x, y = map(int, input().split())
    xToY = y - x #x부터 y까지의 총 거리
    cnt = 1 #이동 장치 작동 횟수
    while xToY > 2 :
        xToY -= 2
        cnt += 1
    else :
        xToY -= 1
        cnt += 1
    print(cnt)
