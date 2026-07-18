from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = Counter(nums)

        index = 0

        for _ in range(freq[0]):
            nums[index] = 0
            index += 1

        for _ in range(freq[1]):
            nums[index] = 1
            index += 1

        for _ in range(freq[2]):
            nums[index] = 2
            index += 1
        return nums