import sys
from io import StringIO

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

n,q = list(map(int,input().split()))

servers = [[] for _ in range(n)]

sums = [0] * n

specifics = {}

def do_sync():
    after_sync_state = [None] * n
    for i in range(0,n-1):
        if not servers[i]:
            continue
        j = 0
        while j < len(servers[i]) and servers[i][j] in servers[i+1]:
            j+=1
        after_sync_state[i] = servers[i][j]


    for i in range(n-1):
        if not after_sync_state[i]: continue
        servers[i+1].append(after_sync_state[i])
        sums[i+1] += specifics[after_sync_state[i]]

id = 1

for i in range(q):
    query = input()
    if query[0] == "a":
        number = int(query.split()[1])
        servers[0].append(id)
        specifics[id] = number
        sums[0] += number
        id+=1
    else:
        do_sync()

print(sum(sums))
