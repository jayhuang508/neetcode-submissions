class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(diff) < 0:
            return -1
        for i in range(len(diff)-1):
            if (diff[i]> 0 and diff[i+1] >0) or diff[i] > abs(diff[i+1]) :
                return i
        return len(diff)-1
        