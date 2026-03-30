class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.res = nums

    def add(self, val: int) -> int:
        self.res.append(val)
        self.res.sort()
        return self.res[len(self.res) - self.k]
