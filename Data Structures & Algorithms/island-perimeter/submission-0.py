class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0):
                return 1
            if (r, c) in visited:
                return 0
            visited.add((r ,c))
            res = 0
            for dr, dc in dir:
                res += dfs(r + dr, c + dc)
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    return dfs(r, c)
        return 0