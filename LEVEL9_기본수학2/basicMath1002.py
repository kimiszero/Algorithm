import math
t = int(input()) #테스트케이스의 개수 t

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2) #두 원의 거리

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue

    if r1 > distance + r2 or r2 > distance + r1 or distance > r1 + r2: 
    #distance가 반지름 더한 값보다 작거나 한 원이 다른 원을 포함하도록 클 때
        print(0)
    elif r1 == distance + r2 or r2 == distance + r1 or distance == r1 + r2:
    #외접하거나 내접할 때
        print(1)
    else:
        print(2)