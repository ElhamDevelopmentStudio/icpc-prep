import math

test_cases = int(input())
x = []

def prime_factors(num):
  nums = []

  for i in range(2, int(math.sqrt(num)) + 1):
    while num % i == 0:
      nums.append(i)
      num = num / i

  if num > 1:
    nums.append(int(num))
  
  nums.sort()
  return nums

for _ in range(test_cases):
  n = int(input())
  factors = prime_factors(n)
  x.append(factors)

for i in x:
  for j in i:
    print(j, end=" ")
  print()