import math

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)+1)):
            if n%i == 0:
                return False
        return True

all_list = list(range(2, 246912))
save_list = []

for i in all_list:
    if isPrime(i):
        save_list.append(i)

n = int(input())
while n != 0:
    count = 0 
    for i in save_list:
        if n < i <= n*2:
            count += 1
    print(count)
    n = int(input())
