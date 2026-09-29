
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = self.build_graph(times)

        heap = [(0, k)]  # (tiempo acumulado, nodo)
        visited = set()
        time = 0

        while heap:
            curr_time, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            time = curr_time

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(
                        heap,
                        (curr_time + weight, neighbor)
                    )

        return time if len(visited) == n else -1

    def build_graph(self, times):
        graph = defaultdict(list)

        for start, end, weight in times:
            graph[start].append((end, weight))

        return graph


times = [[1, 2, 1], [2, 3, 1], [1, 4, 4], [3, 4, 1]]
n = 4
k = 1

solution = Solution()
print(solution.networkDelayTime(times, n, k))  # 3
