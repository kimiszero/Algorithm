while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break

    list = [a, b, c] #리스트에 값을 담아준다. 
    list.sort() # 리스트를 순서대로 정렬한다. 
    print(list)
    if list[2] **2 == list[0] ** 2 + list[1] ** 2:
         print('right')
    else:
        print('wrong')