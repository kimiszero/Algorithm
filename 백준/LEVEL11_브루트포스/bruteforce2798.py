n, m = map(int, input().split()) #n: 카드의 개수 m:10 ~ 300,000아래 정수
cards = list(map(int, input().split()))[:n]
result = 0 #결과값

for a in range(0, n-2): 
    for b in range(a+1, n-1):
        for c in range(b+1, n):
            if (cards[a] + cards[b] + cards[c] > m):
                continue
            else:
                result = max(result, cards[a] + cards[b] + cards[c])

print(result)