X = int(input())
cnt = 0

for i in range(1, X+1):
    if i <= 99 :
        cnt += 1
    else :
        num = list(map(int, str(i)))
        if num[0] - num[1] == num[1] - num[2] :
            cnt += 1
print(cnt)