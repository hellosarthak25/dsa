class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0

        while i < n:
            if nums[i] == val:
                # Shift all elements one position to the left
                for j in range(i, n - 1):
                    nums[j] = nums[j + 1]
                n -= 1
            else:
                i += 1

        return n