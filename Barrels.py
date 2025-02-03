import math

inputAmount = int(input())
literAmount = int(input())

totalLitersPerShift = []

for _ in range(inputAmount):
    
    for i in range(5):
        litersPerShift = list(map(int, input().strip().split()))
        totalLitersPerShift.append(litersPerShift)
        if litersPerShift == " " or litersPerShift == "\n":
            break
    
    totalNum = 0
    for numList in totalLitersPerShift:
        for num in numList:
            totalNum += num
        
    # finalTotal = int(totalNum / literAmount)
    # print(math.ceil(finalTotal))
    print(math.ceil(totalNum / literAmount))
