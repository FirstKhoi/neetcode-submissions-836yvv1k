class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue

                found = False
                for col in range(cols):
                    if col != c and grid[r][col] == 1:
                        found = True
                        break

                if not found:
                    for row in range(rows):
                        if row != r and grid[row][c] == 1:
                            found = True
                            break
                
                if found:
                    res += 1
        return res