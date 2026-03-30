class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = set()
        for num in nums:
            if num in freq:
                freq.remove(num)
            else:
                freq.add(num)
        return list(freq)[0]