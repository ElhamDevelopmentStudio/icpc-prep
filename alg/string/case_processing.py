"""
given a 2D arr of chars 
ur task is to return the smallest minimum distance between two same char
for ex here it is 'E' with the minimum distance of 2
this is my own impl , so no external links
"""
dist = lambda x1,x2,y1,y2 : abs(x1-x2) + abs(y1-y2)

def solve(arr):
    res = float("inf")
    selected = None
    # we keep a location of each char , so for ex for A , i record every i,j of it
    # and everytime i encounter another 'A' after calculating it with previous A's and
    # checking if it is the smallest distance , then we add this A's location
    locations = {}
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            this_loc = locations.get(arr[i][j],None)
            if this_loc == None:
                locations[arr[i][j]] = [[i,j]]
            else:
                for x2,y2 in this_loc:
                    this_min = dist(i,x2,j,y2)
                    if this_min < res: 
                        res = this_min
                        selected = arr[i][j]
                this_loc.append([i,j])
    print(res)
    return selected
            


arr = [
        ['A','F','B','A'],
        ['C','E','G','E'],
        ['B','D','A','F'],
        ['A','C','B','D']
    ]
    
res = solve(arr)
print(res)
