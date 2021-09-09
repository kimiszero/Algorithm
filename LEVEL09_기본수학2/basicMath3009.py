x_list = [] #x좌표를 담을 리스트
y_list = [] #y좌표를 담을 리스트

for i in range(3): #세 점의 좌표를 한 줄씩 입력받아 리스트에 담는다. 
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for i in range(3):
    if x_list.count(x_list[i]) == 1:
        x = x_list[i]
    if y_list.count(y_list[i]) == 1:
        y = y_list[i]

print(x, y)