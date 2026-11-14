class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
        
        return res

        
        #nums = [1,2,3]
        # res = 1
        # i = 2
        # nums[1] = 2