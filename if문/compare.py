# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
A, B = input().split()
A = int(A)
B = int(B)
if (A > B) :
    print('>')
elif (A < B) :
    print('<')
else :
    print('==')