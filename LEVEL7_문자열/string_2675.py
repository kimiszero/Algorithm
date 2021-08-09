T = int(input())
if T >= 1 and T <= 1000 :
    for test in range(T) :
        r, s = map(str, input().split())
        R = int(r)
        if R >= 1 and R <= 8 and len(s) <= 20:
            for char in range(len(s)) :
                print((s[char]*R).strip(), end='')
            print()
