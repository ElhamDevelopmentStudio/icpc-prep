outputs = []
def selectSort(listNum):
  for i in range(len(listNum)):
      minIndex = i
      for j in range(i + 1, len(listNum)):
         if listNum[j] < listNum[minIndex]:
            minIndex = j
      
      if minIndex != i:
         listNum[i], listNum[minIndex] = listNum[minIndex], listNum[i]

  return listNum

for _ in range(int(input())):
  listofNumbers = list(map(int, input().split()))
  outputs.append(selectSort(listofNumbers))

for i in outputs:
  print(i)