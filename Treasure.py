numOfTreasure,maxWeight=list(map(int,input().split()))
weights = []
for i in range(numOfTreasure):
    thisWeight,ThisTreasure=list(map(int,input().split()))
    weights.append([thisWeight,ThisTreasure])
print(weights)
for j in range(weights.__len__()):
    thisArray = []
    weightRn= 0
    dollarRn = 0
    for x in range(weights.__len__()):
        print(x)
        print(weights.__len__())
        if weightRn + weights[x][0] < 50:
            weightRn += weights[x][0]
            dollarRn += weights[x][1]
        if x == weights.__len__():
            print("here")
            thisArray.append([weightRn, dollarRn])
        if weightRn + weights[x][0] > 50 :
            thisArray.append([weightRn, dollarRn])
            weightRn = 0
            dollarRn = 0

    print(thisArray)
