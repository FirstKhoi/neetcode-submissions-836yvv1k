class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        connected = 0

        def dfs(r, c):
            count = 1
            visited.add((r, c))
            for dr in range(rows):
                if grid[dr][c] == 1 and (dr, c) not in visited:
                    count += dfs(dr, c)

            for dc in range(cols):
                if grid[r][dc] == 1 and (r, dc) not in visited:
                    count += dfs(r, dc)
            return count
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    server_size = dfs(r, c)
                    if server_size > 1:
                        connected += server_size
        return connected