outputs = []
for _ in range(int(input())):
  num1, num2 = list(map(str, input().split(":")))

  if num2.find("am") == True:
    print(str(num1) + ":" + str(num2))
    continue
  if num2.find("pm") == True:
    print(str(num1) + ":" + str(num2))
    continue
  
  thisNum1 = int(num1)
  thisNum2 = int(num2)

  if thisNum1 == 0:
    thisNum1 = 12
  if thisNum1 > 12:
    thisNum1 -= 12
  if len(num2) == 1:
    thisNum2 = int(f"0{num2}")

  print(str(thisNum1) + ":" + str(thisNum2))


