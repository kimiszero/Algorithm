T = int(input())

for i in range(T) :
    x, y = map(int, input().split())
    distance = y - x #x부터 y까지의 총 거리
    cnt = 0 #이동 장치 작동 횟수
    move = 1 #cnt별 이동가능한 거리
    total_move = 0 # 이동한 거리의 합
    while total_move < distance :
        cnt += 1
        total_move += move
        if cnt % 2 == 0 :
            move += 1
    print(cnt)