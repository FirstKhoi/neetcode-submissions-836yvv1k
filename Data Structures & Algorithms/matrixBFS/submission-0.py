class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0)) 

        length = 0
        while queue:
            for i in range (len(queue)):
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length
                    
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr == rows or nc == cols or grid[nr][nc] == 1 or (nr, nc) in visit:
                        continue
                    queue.append((nr, nc))
                    visit.add((nr, nc))
            length += 1
        return -1