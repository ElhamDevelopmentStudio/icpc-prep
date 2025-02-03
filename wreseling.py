def wrestle(wreslers):
    
      
    johnCena = wreslers[0]
    underTaker = wreslers[1]
    johnCena = johnCena / 3

    if johnCena > underTaker:
        return "John Cena"
    elif (underTaker > johnCena):
        return "Under Taker"
    


test_case = int(input())

results = []

for _ in range(test_case):
        wreslers = list(map(int, input().split()))
        results.append(wrestle(wreslers))

for _ in results:
    print(_)


