results = []
for _ in range(int(input())):
  thisquery, thislength = list(map(int, input().split()))
  lettersfound = []
  words = []
  importantletters = ['v', 'i', 'k', 'a']
  for s in range(thisquery):
    words.append(list(input()))

  for i in range(len(words)):
    for j in range(len(words[i])):
      if words[i][j] in importantletters and words[i][j] not in lettersfound:
        lettersfound.append(words[i][j])
  
  if len(lettersfound) == 4:
    if lettersfound[0] == importantletters[0] and lettersfound[1] == importantletters[1] and lettersfound[2] == importantletters[2] and lettersfound[3] == importantletters[3]:
      results.append('YES')
    else:
      results.append('NO')
  else:
    results.append('NO')

for i in range(len(results)):
  print(results[i])
