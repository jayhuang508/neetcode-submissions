class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}
        prefix = 0
        count = 0
        for x in nums:
            prefix += x
            count += seen.get(prefix-k, 0)
            seen[prefix] = seen.get(prefix,0)+1
        return count
        