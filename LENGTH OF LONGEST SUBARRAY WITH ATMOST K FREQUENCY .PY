class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        res = 0
        n = len(nums)
        f = {}

        while j < n:
            if nums[j] not in f:
                f[nums[j]] = 1
            else:
                f[nums[j]] += 1

            while f[nums[j]] > k:
                f[nums[i]] -= 1
                i += 1

            res = max(res, j - i + 1)
            j += 1

        return res