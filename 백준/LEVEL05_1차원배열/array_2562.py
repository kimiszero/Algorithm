n_array = []
for i in range(9):
    n_array.append(int(input()))

print(max(n_array))
print(n_array.index(max(n_array))+1)