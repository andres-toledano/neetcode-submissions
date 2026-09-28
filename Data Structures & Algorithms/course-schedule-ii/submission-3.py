from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = self.build_graph(numCourses, prerequisites=prerequisites)
        result = []
        n = len(graph)
        indegree = [0] * n

        for node in range(n):
            for neighbor in graph[node]:
                indegree[neighbor] += 1

        queue = deque()

        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)

        count = 0
        while queue:
            node = queue.popleft()
            result.append(node)
            count += 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if count != n:
            return []
        return result

    def build_graph(self, n, prerequisites):
        graph = defaultdict(list)
        for i in range(n):
            graph[i] = []
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
        return graph