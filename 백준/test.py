n = int(input()) #입력받은 자연수n

def fibo(n):
    a, b = 0, 1
    for i in range(n): 
        yield a
        a, b = b, a + b

if n <= 20 and n >= 0: #자연수n의 조건 : 20보다 작거나 같다.
    for i in enumerate(fibo(n+1)):
       print(i)