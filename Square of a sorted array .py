class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        neg = []
        pos = []

        for i in range(len(nums)):
            if nums[i] >= 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])

        for i in range(len(pos)):
            pos[i] = pos[i] * pos[i]

        for i in range(len(neg)):
            neg[i] = neg[i] * neg[i]

        neg.reverse()

        if len(pos) == 0:
            return neg
        if len(neg) == 0:
            return pos

        n = len(neg)
        m = len(pos)

        i = 0
        j = 0
        idx=0

        while i < n and j < m:
            if neg[i] <= pos[j]:
                nums[idx]=neg[i]
                idx+=1
                i += 1
            else:
                nums[idx]=pos[j]
                idx+=1
                j += 1

        while i < n:
            nums[idx]=neg[i]
            idx+=1
            i += 1

        while j < m:
            nums[idx]=pos[j]
            idx+=1
            j += 1

        return nums