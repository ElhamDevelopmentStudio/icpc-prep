outputs =[]
for _ in range(int(input())):
    thisSequence = int(input())
    thisSequenceNumbers = [0, 1, 1]
    if thisSequence == 3:
        pass
    for i in range(2,thisSequence):
        thisArray = []
        thisArray.append(thisSequenceNumbers[i])
        thisArray.append(thisSequenceNumbers[i-1])
        thisArray.append(thisSequenceNumbers[i-2])
        thisSequenceNumbers.append(sum(thisArray))
    outputs.append(thisSequenceNumbers[-1])
print("\n".join(str(x) for x in outputs))



