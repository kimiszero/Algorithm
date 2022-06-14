A = int(input())
B = int(input())
C = int(input())
if((A >= 100 and B >=100 and C >= 100) and (A < 1000 and B < 1000 and C < 1000)): 
    mul = A * B * C
    arr = list(str(mul))
    for i in range(10) :
        count = arr.count(str(i))
        print(count)

