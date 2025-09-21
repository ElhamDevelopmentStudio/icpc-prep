"""
given a normal building as 0 and a explosive one as 1
cout how many buildings survive

a explosive building will explode a building to his right and a building to his left
"""



for _ in range(int(input())):
    building = list(input())
    output = [ True if b == "1" else False for b in building ]

    for i in range(len(building)):
        if building[i] == "1":
            if i == 0:
                output[i+1]= True
            elif i == len(building) -1:
                output[i-1] = True
            else:
                output[i+1]= True
                output[i-1] = True

    result = 0
    for r in output:
        if not r:
            result += 1

    print(result)
