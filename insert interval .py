class Solution:
    def insert(self, nums: List[List[int]], newinterval: List[int]) -> List[List[int]]:
        new = []
        insert = False
        n = len(nums)
        res = []

        for i in range(n):
            start = nums[i][0]

            if insert == False and start >= newinterval[0]:
                new.append(newinterval)
                insert = True

            new.append(nums[i])

        if insert == False:
            new.append(newinterval)

        start1 = new[0][0]
        end1 = new[0][1]

        for i in range(1, len(new)):
            start2 = new[i][0]
            end2 = new[i][1]

            if end1 >= start2:
                end1 = max(end1, end2)
                continue

            res.append([start1, end1])
            start1 = start2
            end1 = end2

        res.append([start1, end1])

        return res