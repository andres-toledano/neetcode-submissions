class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        curr_word = []
        found = [False]
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        def dfs(r, c):
            visited.add((r, c))
            curr_word.append(board[r][c])

            if len(curr_word) == len(word):
                solution = "".join(curr_word)
                if solution == word:
                    found[0] = True
                curr_word.pop()
                visited.remove((r,c))
                return

            
            for move in moves:
                new_r = r + move[0]
                new_c = c + move[1]
                if 0 <= new_r <= len(board) - 1 and 0 <= new_c <= len(board[0]) - 1 and (new_r, new_c) not in visited:
                    dfs(new_r, new_c)
            curr_word.pop()
            visited.remove((r,c))
                    

        for r in range(len(board)):
            for c in range(len(board[0])):
                if not found[0]:
                    dfs(r, c)
        return found[0]
                 





        