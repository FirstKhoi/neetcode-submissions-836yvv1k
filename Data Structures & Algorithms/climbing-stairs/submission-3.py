class Solution:
    def climbStairs(self, n: int) -> int:
        res = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
            if res[i] != -1:
                return res[i]
            res[i] = dfs(i + 1) + dfs(i + 2)
            return res[i]
        return dfs(0)