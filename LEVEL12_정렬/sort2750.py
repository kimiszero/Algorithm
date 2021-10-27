n = int(input()) #입력받을 수의 개수 n
n_list = []
n_list2 = []
for i in range(n):
    a = int(input())
    n_list.append(a)

n_list2 = sorted(n_list)
for i in n_list2:
    print(i)