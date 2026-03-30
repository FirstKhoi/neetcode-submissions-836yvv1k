class Solution:
    def rob(self, nums: List[int]) -> int:
        robA, robB = 0, 0
        for num in nums:
            temp = max(num + robA, robB)
            robA = robB
            robB = temp
        return robB