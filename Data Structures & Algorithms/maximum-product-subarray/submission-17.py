class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP, minP = 1, 1
        res = max(nums)

        for n in nums:
            tmp = maxP * n
            maxP = max(n, maxP * n, minP * n)
            minP = min(n, minP * n, tmp)

            res = max(res, maxP)
        
        return res