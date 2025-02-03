palindromeCounter = 0
for _ in range(int(input())):
    thisWord=input()
    if thisWord == thisWord[::-1]:
        palindromeCounter += 1
print(palindromeCounter)
