import sys

N = int(sys.stdin.readline())
if(N >= 1 and N <= 1000000) :
    num_list = list(map(int, sys.stdin.readline().split(maxsplit=N)))
    print(min(num_list), max(num_list))