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

# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

A = int(input())
if(A < 101 and A => 0): 
    if(A <= 100 and A >= 90) : 
        print('A')
    elif(A <= 89 and A >= 80) :
        print('B')
    elif(A <= 79 and A >= 70) :
        print('C')
    elif(A <= 69 and A >= 60) :
        print('D')
    else :
        print('F')
else :
    print('시험 점수는 0점과 100점 범위 내에서 입력하세요')