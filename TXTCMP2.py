for _ in range(int(input())):
  num, word = list(map(str, input().split()))
  num = int(num)
  word = word.strip()

  j = 0
  nums = {}
  result = ''

  while j < len(word):
    cmp = word[j:j + num]
    if cmp not in nums:
      nums[cmp] = str(len(nums) + 1)
    
    result += nums[cmp]
    j += num
  
  print(result)