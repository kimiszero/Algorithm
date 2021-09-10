n = int(input()) #입력받은 자연수n 

def fibonacci(n): #피보나치 함수
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if n <= 20 and n >= 0: #자연수n의 조건 : 20보다 작거나 같다.
    print(fibonacci(n))