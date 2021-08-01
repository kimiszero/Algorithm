n = int(input())

for i in range(n):
    test_list = list(input())
    score = 0
    sum = 0
    for test in test_list : 
        if test == 'O':
            score += 1
            sum += score    
        else:
            score = 0
    print(sum)