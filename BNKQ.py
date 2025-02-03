class queue:
  def __init__(self):
    self.q = []

  def push(self, element):
    self.q.append(element)
    self.q.sort()
  
  def pop(self):
    self.q.pop(0)
  
  def empty(self):
    return len(self.q) == 0



for _ in range(int(input)):
  counter, numOfCustomers = list(map(int, input().split()))

  for i in range(numOfCustomers):
    minArrival, minFinish = int(input())
    

