#입력받은 원판의 개수 n
#a : 옮길 원반이 있는 출발점
#b : 원반을 옮길 도착점
#c : 옮기는 중간 과정 임시점

def hanoi(n, a, b, c):
    if n == 1: #원반이 하나인 경우
        move.append([a, c])
        return 
    else:
        hanoi(n-1, a, c, b)
        move.append([a, c])
        hanoi(n-1, b, a, c)

move = [] #이동경로를 담을 list
n = int(input())
hanoi(n, 1, 2, 3) 

print(len(move))
print('\n'.join([' '.join(str(i) for i in row) for row in move])) #이동경로 출력