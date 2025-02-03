outputs = []
def insertionSort(listofNumbers):
  for i in range(len(listofNumbers)):
    j = i - 1
    while listofNumbers[j] > listofNumbers[j + 1] and j >= 0:
      listofNumbers[j], listofNumbers[j + 1] = listofNumbers[j + 1], listofNumbers[j]
      j -= 1
  
  return listofNumbers

for _ in range(int(input())):
  listofNumbers = list(map(int, input().split()))
  outputs.append(insertionSort(listofNumbers))

for i in outputs:
  print(i)