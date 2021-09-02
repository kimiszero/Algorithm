#입력값은 10000까지 주어지며 0, 1번 인덱스는 False인 소수리스트를 만든다. 
prime_list = [False, False] + [True]*10002

for i in range(2, 10002):
    if prime_list[i]:
        #소수를 구하기 위해 반복문을 돌린다. 10002보다 작지만 2의 배수들은 소수가 아니니 False값을 담는다. 
        for j in range(2*i, 10002, i):
            prime_list[j] = False

T = int(input()) #입력받는 테스트 케이스의 개수 T

for i in range(T):
    n = int(input()) #입력받는 짝수 n
    a = n // 2 #입력받은 짝수의 중간값을 만들어 탐색한다.
    b = a
    while a > 0:
        if prime_list[a] and prime_list[b]:
            print(a, b)
            break
        else:
            a -= 1
            b += 1