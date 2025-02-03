outputs= []
costsArray = []
for _ in range(int(input())):
    row,column = list(map(int,input().split()))
    coms = []
    comCost = {}
    comNames=[]

    for i in range(column):
        com1,com2,cost = list(map(int,input().split()))
        if com1 not in coms:
            coms.append(com1)
        if com2 not in coms:
            coms.append(com2)
        comNames.append([com1,com2])
        comCost[com1,com2]= cost
    for i in range(comCost.__len__()):
        totalComputersFound = []
        cost = 0
        for j in range(i,comNames.__len__()):
            cost += comCost[comNames[j][0],comNames[j][1]]
            if comNames[j][0] not in totalComputersFound:
                totalComputersFound.append(comNames[j][0])
            if comNames[j][1] not in totalComputersFound:
                totalComputersFound.append(comNames[j][1])

            if totalComputersFound.__len__() == coms.__len__():
                costsArray.append(cost)
                cost = 0
                break
    outputs.append(min(costsArray))
print("\n".join(str(outputs[x]) for x in range(outputs.__len__())))