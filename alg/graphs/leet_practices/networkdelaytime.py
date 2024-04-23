import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = {}
        for nodea, nodeb, time in times:
            if nodea in graph:
                graph[nodea].append((nodeb, time))
            else:
                graph[nodea] = [(nodeb, time)]
        dist = {node: float("inf") for node in range(1, n+1)}
        dist[k] = 0
        queue = [(0, k)]
        while queue:
            curr_time, curr_node = heapq.heappop(queue)
            if curr_time > dist[curr_node]:
                continue
            for neigh, n_time in graph.get(curr_node, []):
                this_sum = curr_time + n_time
                if this_sum < dist[neigh]:
                    dist[neigh] = this_sum
                    heapq.heappush(queue, (this_sum, neigh))
        max_ = -1
        for time_ in dist.values() : max_ = max(time_,max_)
        return -1 if max_ == float("inf") else max_ # type: ignore