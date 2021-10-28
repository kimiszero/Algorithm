import sys

n = int(input()) #입력받는 수의 개수 n
unsorted_list = []
sorted_list = []

for i in range(n): 
    a = int(sys.stdin.readline())
    unsorted_list.append(a)

sorted_list = sorted(unsorted_list)
for i in sorted_list:
    sys.stdout.write(str(i)+'\n')