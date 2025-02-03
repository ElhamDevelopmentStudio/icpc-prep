outputs = []
for _ in range(int(input())):
    row, column = list(map(int, input().split()))
    coms = []
    comCost = {}
    comNames = []
    thisProbability = []
    for i in range(column):
        com1, com2, cost = list(map(int, input().split()))
        if com1 not in coms:
            coms.append(com1)
        if com2 not in coms:
            coms.append(com2)
        comNames.append([com1, com2])
        comCost[com1, com2] = cost
    for i in range(comCost.__len__()):
        startingIndex = i + 1
        key = comNames[i]
        value = comCost[key[0], key[1]]
        endReached = False
        computersFound = [key[0], key[1]]
        if i + 1 == comCost.__len__():
            endReached = True
        while endReached == False:

            for j in range(startingIndex, comCost.__len__()):
                # print(f"at i {i} and j {j}")
                if j == comCost.__len__() - 1:
                    if comNames[j][0] not in computersFound:
                        computersFound.append(comNames[j][0])
                    if comNames[j][1] not in computersFound:
                        computersFound.append(comNames[j][1])
                    if computersFound.__len__() == coms.__len__():
                        thisProbability.append(
                            value + comCost[comNames[j][0], comNames[j][1]])
                    endReached = True
                    break
                value += comCost[comNames[j][0], comNames[j][1]]
                if comNames[j][0] not in computersFound:
                    computersFound.append(comNames[j][0])
                if comNames[j][1] not in computersFound:
                    computersFound.append(comNames[j][1])
                if computersFound.__len__() == coms.__len__():

                    startingIndex = j + 1
                    thisProbability.append(value)
                    print("here")
                    value = comCost[key[0], key[1]]
                    break
    print(thisProbability)
    outputs.append(min(thisProbability))
print(*outputs)
