dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
s = input()
time = 0
for j in range(len(s)) :
    for i in dial :
        if s[j] in i :
            time += dial.index(i) + 3
print(time)