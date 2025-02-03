test_case = int(input())
x = []

for i in range(test_case):
    word1 = input()
    word2 = input()
    for j in range(len(word1)):
        for p in range(len(word2)):
            if word1[j] == word2[p]:
                x.append(word2[p])

# x = set(x)

p = set(x)

print(p)