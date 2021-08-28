M, N = map(int, input().split())
arr=[]

for i in range(M,N+1):
    if i == 1:
        pass
    elif i == 2:
        arr.append(i)
    else:
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i - 1:
                arr.append(i)

for i in arr:
    print(i)