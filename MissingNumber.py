output = []
for _ in range(int(input())):
    foundNumber = False
    thisArrayLen = int(input())
    thisArray = list(map(int,input().split()))
    thisArray.sort()
    thismax = max(thisArray)
    for i in range(0,thismax):
        if i not in thisArray:
            output.append(i)
            foundNumber = True
            break
    if foundNumber == False:
        output.append(thismax+1)
print("\n".join(str(output[x]) for x in range(output.__len__())))