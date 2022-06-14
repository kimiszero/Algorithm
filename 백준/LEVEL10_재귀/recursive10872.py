#재귀함수 사용
def factorial(n):
    if(n > 1):
        return n * factorial(n-1)
    else:
        return 1

n = int(input())
if n >= 0 and n <= 12: #조건: 정수n은 0과 크거나 같고 12보다 작거나 같다.
    print(factorial(n))