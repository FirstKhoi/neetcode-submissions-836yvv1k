class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n, res = len(nums), []

        for i in range(n):
            check = True
            for j in range(n):
                if i != j and nums[i] == nums[j]:
                    check = False
                    break
            if check:
                res.append(nums[i])
                if len(res) == 2:
                    break
        return res