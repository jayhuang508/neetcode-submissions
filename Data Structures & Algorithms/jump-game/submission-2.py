class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # max jump distance, check whether the whole array could be covered
        covered = [False] * len(nums)
        for i, num in enumerate(nums):
            if i+num < len(nums):
                for j in range(i, i+num):
                    
                    covered[j] = True
                if i+num+1 == len(nums):
                    covered[-1] = True
            else:
                for j in range(i, len(nums)):
                    covered[j] = True
        for v in covered:
            if v == False:
                print(v)
                return False
        return True

        