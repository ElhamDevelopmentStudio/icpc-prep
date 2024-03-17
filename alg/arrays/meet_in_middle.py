def sum_of_subsets(arr):
    result = []
    for i in range(1<<len(arr)):
        subs = []
        for j in range(len(arr)):
            if i & (1 << j):
                subs.append(arr[j])
        result.append(sum(subs))
    return result

n = [2,4,5,9]
x = 15

# 3 2

middle = (len(n) // 2) - 1
A = n[:middle+1]
B = n[middle+1:]

print(A)
print(B)
Sa = sum_of_subsets(A)
Sb = sum_of_subsets(B)

for i in range(len(Sa)):
    if Sa[i] + Sb[i] == x:
        print(f"possible with {Sa[i]} {Sb[i]}")



