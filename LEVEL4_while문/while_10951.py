import sys
while True :
    try:
        A,B = map(int, sys.stdin.readline().split())
    except :
        break
    else :
        if(A > 0 and B < 10):
            print(A+B)