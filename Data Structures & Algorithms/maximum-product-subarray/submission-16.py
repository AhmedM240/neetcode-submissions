class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minP, maxP = 1,1
        res = max(nums)

        for n in nums:
            tmp = maxP * n
            maxP = max(maxP * n, n, minP * n)
            minP = min(minP * n, n, tmp)
            res = max(res, maxP)
        
        return res