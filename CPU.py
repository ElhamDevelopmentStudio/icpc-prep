
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
    num_tasks = int(input())
    start_times = list(map(int, input().split()))
    finish_times = list(map(int, input().split()))

    jobs = []
    for i in range(num_tasks):
        jobs.append((start_times[i], finish_times[i]))

    jobs.sort(key=lambda x: x[1])

    pq = PriorityQueue()
    cpus_required = 0

    for start, finish in jobs:
        if pq.empty():
            pq.push(finish)
            cpus_required += 1
        else:
            earliest_finish = pq.pop()
            if start >= earliest_finish:
                pq.push(finish)
            else:
                pq.push(earliest_finish)
                pq.push(finish)
                cpus_required += 1

    outputs.append(cpus_required)

for i in outputs:
    print(i)
