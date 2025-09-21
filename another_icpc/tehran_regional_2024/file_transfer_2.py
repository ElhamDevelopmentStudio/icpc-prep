import sys
from io import StringIO

#print = sys.stdout.write

input_string = """3 7
add 1
add 2
sync
add 1
add 2
sync
sync
"""

sys.stdin = StringIO(input_string)

lines = sys.stdin.readlines()
ptr = 0

n,q = list(map(int,lines[0].split()))
ptr+= 1

servers = [[] for _ in range(n)]
specifics = {}

sums = [0] * n
"""
id => size
"""

id = 1

def do_sync():
    """
    1 2 3
    1   
    2
    """

    sync_state = [None] * n
    
    for i in range(n-1):
        for j in range(len(servers[i])):
            if servers[i][j] not in servers[i+1]:
                sync_state[i] = servers[i][j]
                break


    #print(sync_state) 
    for i in range(n-1):
        if sync_state[i]:
            servers[i+1].append(sync_state[i])
            sums[i+1] += specifics[sync_state[i]]


for _ in range(q):
    query = lines[ptr]
    ptr+= 1
    
    if query[0] == "a":
        number = int(query.split()[1])
        servers[0].append(id)
        specifics[id] = number
        sums[0] += number
        id+=1
    else:
        do_sync()
    
    from pprint import pp
    pp(servers)
    pp(str(sum(sums)))


