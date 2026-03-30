class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] 

        visited_pacific = set()
        visited_atlantic = set()
        
        def dfs(r, c, visited_set, prev_height):
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                (r, c) in visited_set or 
                heights[r][c] < prev_height):
                return
            
            visited_set.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited_set, heights[r][c])
                
        for r in range(rows):
            dfs(r, 0, visited_pacific, heights[r][0])
            dfs(r, cols - 1, visited_atlantic, heights[r][cols - 1])

        for c in range(cols):
            dfs(0, c, visited_pacific, heights[0][c])
            dfs(rows - 1, c, visited_atlantic, heights[rows - 1][c])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in visited_pacific and (r, c) in visited_atlantic:
                    res.append([r, c])
        return res