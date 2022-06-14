A, B = input().split()
A = A[::-1]
B = B[::-1]
if A != B :
    if int(A) > int(B) :
        print(A)
    else :
        print(B)