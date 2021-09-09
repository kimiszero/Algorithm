import sys
A,B = map(int, sys.stdin.readline().split())
while A > 0 and B < 10 :
    print(A+B)
    A,B = map(int, sys.stdin.readline().split())
    if A == 0 and B == 0 :
        break