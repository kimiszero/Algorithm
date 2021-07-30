cnt = 0
i_arr = []
for i in range(10) :
    i = int(input())
    if(i > 0 and i <= 1000):
        a = i % 42
        i_arr.append(a)
cnt = set(i_arr)
print(len(cnt))