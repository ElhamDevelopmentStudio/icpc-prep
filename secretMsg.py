alphaDict = {
  "1": "1", "2": "2", "22": "a", "222": "b", "2222": "c", 
  "3": "3", "33": "d", "333": "e", "3333": "f",
  "4": "4", "44": "g", "444": "h", "4444": "i",
  "5": "5", "55": "j", "555": "k", "5555": "l",
  "6": "6", "66": "m", "666": "n", "6666": "o", 
  "7": "7", "77": "p", "777": "q", "7777": "r", "77777": "s",
  "8": "8", "88": "t", "888": "u", "8888": "v",
  "9": "9", "99": "w", "999": "x", "9999": "y", "99999": "z" 
}

def secretMessage(msg):
  decrypted = ""
  for code in msg:
    if code in alphaDict:
      decrypted += alphaDict[code]
    else:
      decrypted += "?"
  return decrypted

test_cases = int(input())
for _ in range(test_cases):
  msg = input().split()
  print(secretMessage(msg))