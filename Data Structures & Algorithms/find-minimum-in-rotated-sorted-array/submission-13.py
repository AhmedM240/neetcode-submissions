class Solution:
    def findMin(self, nums: List[int]) -> int:
        minV = nums[0]

        l,r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                minV = min(minV, nums[m])
                r = m - 1
        
        return minV