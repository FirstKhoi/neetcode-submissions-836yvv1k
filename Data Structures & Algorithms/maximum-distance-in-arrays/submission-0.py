class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        n = len(arrays)
        for i in range(n - 1):
            for j in range(i + 1, n):
                arr1 = arrays[i]
                arr2 = arrays[j]
                res = max(res, abs(arr1[0] - arr2[-1]))
                res = max(res, abs(arr2[0] - arr1[-1]))
        return res