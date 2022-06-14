x,y,w,h = map(int, input().split()) #입력받는정수 w,y,w,h

print(min(x, y, w-x, h-y))