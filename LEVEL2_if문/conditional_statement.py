# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
# A, B = input().split()
# A = int(A)
# B = int(B)
# if (A > B) :
#     print('>')
# elif (A < B) :
#     print('<')
# else :
#     print('==')

#update_0814
# A, B = map(int, input().split(' '))
# if A > B :
#     print('>')
# elif A < B :
#     print('<')
# else :
#     print('==')

# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
# A = int(input())
# if(A < 101 and A >= 0): 
#     if(A <= 100 and A >= 90) : 
#         print('A')
#     elif(A <= 89 and A >= 80) :
#         print('B')
#     elif(A <= 79 and A >= 70) :
#         print('C')
#     elif(A <= 69 and A >= 60) :
#         print('D')
#     else :
#         print('F')
# else :
#     print('시험 점수는 0점과 100점 범위 내에서 입력하세요')

# 2753번 윤년
#연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
# 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 하지만, 2000년은 400의 배수이기 때문에 윤년이다.
# year = int(input())
# if(year%4 ==0 and (year%100!=0 or year%400==0) ) :
#     print('1')
# else:
#     print('0')

# 사분면 고르기
# 흔한 수학 문제 중 하나는 주어진 점이 어느 사분면에 속하는지 알아내는 것이다. 사분면은 아래 그림처럼 1부터 4까지 번호를 갖는다. "Quadrant n"은 "제n사분면"이라는 뜻이다.
# x = int(input()) 
# y = int(input())
# if x >= -1000 and x <= 1000 and x != 0 and y >= -1000 and y <= 1000 and y != 0 : 
#     if x > 0 and y > 0 :
#         print('1')
#     elif x < 0 and y > 0 :
#         print('2')
#     elif x < 0 and y < 0 :
#         print('3')
#     else :
#         print('4')

# 알람시계
H, M = map(int, input().split())
if H >= 0 and H <= 23 and M >= 0 and M <= 59 :
   if H == 0 :
       if M < 45 :
        print(24-1, M+15)
       else :
        print(H, M-45) 
   else :
       if M >=45 :
        print(H, M-45) 
       else :
        print(H-1, M+15)
else :
    print('24시간 기준으로 입력하세요')