class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        p1 = 0
        p2 = n - 1

        last1 = nums[0]
        last2 = nums[1]

        res[p1] = nums[0]
        p1 += 1

        res[p2] = nums[1]
        p2 -= 1

        for i in range(2, n):
            if last1 > last2:
                res[p1] = nums[i]
                p1 += 1
                last1 = nums[i]
            else:
                res[p2] = nums[i]
                p2 -= 1
                last2 = nums[i]

        # reverse the second part
        left = p1
        right = n - 1

        while left < right:
            res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1

        return res