class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            grid[i][j] = "0"
            steps = [(-1, 0), (1, 0), (0, 1), (0, -1)]

            for dr, dc in steps:
                new_r = i + dr
                new_c = j + dc

                if (
                    0 <= new_r < len(grid)
                    and 0 <= new_c < len(grid[0])
                    and grid[new_r][new_c] == "1"
                    ):
                        dfs(new_r, new_c)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count