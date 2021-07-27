N = int(input())

if(N >= 1 and N <= 1000000) :
    n_list = list(map(int, input().split(maxsplit=N)))
    print(min(n_list), max(n_list))