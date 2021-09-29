n = int(input()) #입력받은 자연수 n

for i in range(1, n+1):
    arr = list(map(int, str(i)))
    if sum(arr) + i == n:
        print(i)
        break
    if i == n:
        print(0)
        break