
class PriorityQueue:
    def __init__(self):
        self.pq = []

    def push(self, element):
        self.pq.append(element)
        self.pq.sort()

    def pop(self):
        return self.pq.pop(0)

    def empty(self):
        return len(self.pq) == 0


outputs = []

for _ in range(int(input())):
  tasks = int(input())
  startTimes = list(map(int, input().split()))
  finishTimes = list(map(int, input().split()))

  jobs = []
  cpu = 0

  for i in range(tasks):
      jobs.append((startTimes[i], finishTimes[i]))

  jobs.sort(key=lambda x: x[1])

  pq = PriorityQueue()

  for start, finish in jobs:
      if pq.empty():
          pq.push(finish)
          cpu += 1
      else:
          newFinish = pq.pop()
          if newFinish <= start:
              pq.push(finish)
          else:
              pq.push(newFinish)
              pq.push(finish)
              cpu += 1

  outputs.append(cpu)

for i in outputs:
    print(i)
