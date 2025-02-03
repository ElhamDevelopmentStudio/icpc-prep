results = []
for _ in range(int(input())):
  num, word = list(map(str, input().split()))
  num = int(num)
  word.strip()
  j = 0

  total = {}
  result = ''
  while j < len(word):
    t = word[j:j + num]
    if t not in total:
      total[t] = str(len(total) + 1)

    result += total[t]
    j += num

  results.append(result)



for i in results:
  print(i)
  