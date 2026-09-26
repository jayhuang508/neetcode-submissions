class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur = nums[0]
        for i in range(1, len(nums)):
            cur += nums[i]
            if cur < 0:
                cur = 0
                res = max(res, nums[i]) 
            else:
               res = max(res, cur) 
        return res


        
        