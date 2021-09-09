all_number = set(range(1, 10001))
generated_number = set()

for i in range(1, 10001) :
    for j in str(i) :
        i += int(j);
    generated_number.add(i)

self_number = sorted(all_number - generated_number)
for i in self_number :
    print(i)