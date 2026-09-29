from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        graph = self.build_graph(wordList)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            node, count = queue.popleft()
            if node == endWord:
                return count

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, count + 1))
                    visited.add(neighbor)

        return 0


        
    def build_graph(self, words: List[str]):
        graph = defaultdict(list)
        for word1 in words:
            neighbors = []
            for word2 in words:
                if self.differs_by_one(word1, word2):
                    neighbors.append(word2)
            graph[word1] = neighbors
        return graph

    def differs_by_one(self, word1, word2) -> bool:
        if len(word1) != len(word2):
            return False
        
        return sum(a != b for a, b in zip(word1, word2)) == 1


                
        