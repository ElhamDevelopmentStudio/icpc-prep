for _ in range(int(input())):
    lenght = int(input())
    word1 = input()
    word2 = input()
    equal = False

    for i in range(len(word1)):

        while equal != True:
            t = word1[i + 1]
            word1[i + 1] = word1[i]
            word1[i] = t

            p = word2[i + 1]
            word2[i + 1] = word2[i]
            word2[i] = p


print(word1, word2)
