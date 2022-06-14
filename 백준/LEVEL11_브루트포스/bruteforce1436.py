n = int(input()) #입력받은 자연수 n
count = 0
six_n = 666
while True:
    if '666' in str(six_n):      #1부터 n까지 모든 수를 대입하기 위해 count를 사용한다.
        count += 1          
    if count == n:          # 카운트와 n번째 수가 같으면 six_n을 출력한다. 
        print(six_n)        
        break
    six_n += 1                  #666이 포함된 수가 나올 때까지 six_n을 증가시킨다. 