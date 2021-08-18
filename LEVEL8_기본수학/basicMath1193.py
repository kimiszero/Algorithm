X = int(input())

line = 0 
max = 0
while X > max :
    line += 1
    max += line

gap = max - X
if line % 2 == 0 :
    top = line - gap
    under = gap + 1
else :
    top = gap + 1
    under = line - gap
print(f'{top}/{under}')