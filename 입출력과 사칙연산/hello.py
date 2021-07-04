# Hello Python
print('Hello Python')

# 고양이 
print('\\    /\\')
print(' )  ( \')')
print('(  /  )')
print(' \\(__)|')
    
# 강아지
print('|\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\__|')

# 사칙연산 
a, b = input().split()
a = int(a)
b = int(b)
print(a+b, a-b, a*b, int(a/b), a%b, sep='\n')

# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

A, B, C = map(int, input().split())
print((A+B)%C, ((A%C) + (B%C))%C, (A*B)%C, ((A%C) * (B%C))%C, sep='\n')