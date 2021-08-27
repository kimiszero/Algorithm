N = int(input())
num = 2

while True:
    if N % num == 0:
        N = N // num
        print(num)
    elif N == 1:
        break
    else:
        num += 1
