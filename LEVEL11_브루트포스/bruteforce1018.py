n, m = map(int, input().split()) #n & m: 8 ~ 50 사이의 자연수
origin = [] #처음 판을 저장하기 위한 리스트
count = [] #바뀐 판의 갯수를 저장하기 위한 리스트

for _ in range(n): #입력받은 n만큼 한줄씩 리스트에 넣는다.
    origin.append(input())

for a in range(n-7): #n과 m이 8보다 클 시, 큰 숫자만큼 1씩 더해준다.
    for b in range(m-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if origin[i][j] != 'W': 
                        index1 += 1
                    else:
                        index2 += 1
                else:
                    if origin[i][j] != 'B':
                        index1 += 1
                    else:
                        index2 += 1
        count.append(min(index1, index2))
print(min(count))