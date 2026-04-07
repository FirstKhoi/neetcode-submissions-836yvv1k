class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        s, e = n - 1, 0
        tank = gas[s] - cost[s]
        while s > e:
            if tank < 0:
                s -= 1
                tank += gas[s] - cost[s]
            else:
                tank += gas[e] - cost[e]
                e += 1
        return s if tank >= 0 else - 1 