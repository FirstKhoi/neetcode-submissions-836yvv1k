class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == "O":
                    q.append((r, c))
                    board[r][c] = "T"
        while q:
            r, c = q.popleft()
            for dr, dc in dir:
                nr , nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    board[nr][nc] = "T"
                    q.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"