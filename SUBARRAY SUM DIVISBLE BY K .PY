class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        f = {}
        ans = 0
        sum = 0

        f[0] = 1

        for i in range(len(nums)):
            sum += nums[i]

            rem = sum % k

            if rem < 0:
                rem += k

            if rem in f:
                ans += f[rem]
                f[rem] += 1
            else:
                f[rem] = 1

        return ans