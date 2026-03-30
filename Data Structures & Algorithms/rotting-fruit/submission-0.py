class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        mins = -1
        fresh_count = 0
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0: return 0
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        while queue:
            mins += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
        
        return mins if fresh_count == 0 else -1