"""
given a matrix just rotate it 90*
meaning 
input:
1,2,3
4,5,6
7,8,9

output:
7,4,1
8,5,2
9,6,3
"""


num_of_rows = int(input())

matrix = []
for _ in range(num_of_rows):
    matrix.append(
        list(map(int,input().split(",")))
    )

output = []

for i in range(num_of_rows):
    local_matrix = []

    for j in reversed(range(num_of_rows)):
        local_matrix.append(matrix[j][i])

    output.append(local_matrix)


for o in output:
    out_out = ""
    for w in range(len(o)):
        out_out += f"{o[w]}, "

    out_out = out_out[:-2]
    print(out_out)
