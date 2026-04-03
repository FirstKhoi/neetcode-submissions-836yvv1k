class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_so_far = nums[0]

        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum > max_so_far:
                max_so_far = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return max_so_far