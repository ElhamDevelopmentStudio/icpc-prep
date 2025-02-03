
n = int(input())
size = n - 1

treeInput = []
qInput = []
for i in range(n - 1):
    tree = input().split()
    
    treeInput.append(tree)
    
for i in range(size):
  q = int(input())
  if q not in qInput:
          qInput.append(q)

ones = []
twos =[]
threes = []
fours = []
fives = []
sixs = []

for i in treeInput:
    for j in i:
        if (j == '1'):
            p = ones.append(i[1])
        elif (j == '2'):
            p = twos.append(i[1])
        elif (j == '3'):
            p = threes.append(i[1])
        elif (j == '4'):
            p = fours.append(i[1])
        elif (j == '5'):
            p = fives.append(i[1])
        elif (j == '6'):
            p = sixs.append(i[1])


print(qInput)