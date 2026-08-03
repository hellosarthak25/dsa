class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxend = nums[0]
        minend = nums[0]
        res = abs(nums[0])

        n = len(nums)

        for i in range(1, n):
            v1 = nums[i]
            v2 = nums[i] + maxend
            maxend = max(v1, v2)

            v3 = nums[i] + minend
            minend = min(v1, v3)

            res = max(res, abs(maxend), abs(minend))

        return res