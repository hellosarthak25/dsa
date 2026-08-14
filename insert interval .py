class Solution:
    def merge(self, nums: List[List[int]]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        start1 = nums[0][0]
        end1 = nums[0][1]

        for i in range(1, n):
            start2 = nums[i][0]
            end2 = nums[i][1]

            if end1 >= start2:
                end1 = max(end1, end2)
                continue

            res.append([start1, end1])
            start1 = start2
            end1 = end2

        res.append([start1, end1])

        return res