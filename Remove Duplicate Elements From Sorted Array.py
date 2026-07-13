class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        res=1
        j=1
        while j<len(nums):
            if nums[j]==nums[j-1]:
                j=j+1
                continue
            else:
                nums[i+1]=nums[j]
                i=i+1
                j=j+1
                res=res+1
        return res