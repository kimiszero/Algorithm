n = int(input())
nums = list(input())
sum = 0
if n >= 0 and n <= 100 :
    for i in nums :
       sum += int(i)
print(sum)