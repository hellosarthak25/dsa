class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        bestending1 = nums[0]
        bestending2 = nums[0]

        res = nums[0]
        minsum = nums[0]

        summ = sum(nums)

        for i in range(1, len(nums)):
            bestending1 = max(bestending1 + nums[i], nums[i])
            res = max(res, bestending1)

            bestending2 = min(bestending2 + nums[i], nums[i])
            minsum = min(minsum, bestending2)

        if res < 0:
            return res

        return max(res, summ - minsum)