class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in resMap:
                return [resMap[diff], i]
            resMap[n] = i