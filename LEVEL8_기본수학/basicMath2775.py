T = int(input())
for i in range(T) :
    k = int(input()) # 층수
    n = int(input()) # 호수
    people = [i for i in range(1, n+1)]

    for x in range(k) :
        for y in range(1, n) :
            people[y] += people[y-1]
    print(people[-1])