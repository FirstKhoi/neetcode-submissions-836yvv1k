class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            res = nums.count(num)
            if res > len(nums) / 2:
                return num