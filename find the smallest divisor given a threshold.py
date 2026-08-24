from math import ceil

class Solution:
    def possible(self, nums, guess, t):
        check = 0

        for i in range(len(nums)):
            check += ceil(nums[i] / guess)

        if check <= t:
            return True
        return False

    def smallestDivisor(self, nums, threshold):
        low = 1
        high = max(nums)
        res = -1

        while low <= high:
            guess = (low + high) // 2

            if self.possible(nums, guess, threshold):
                res = guess
                high = guess - 1
            else:
                low = guess + 1

        return res