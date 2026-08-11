class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        summ=nums[0]
        i=1
        while i<len(nums) and nums[i]==nums[i-1]+1:
            summ+=nums[i]
            i+=1
        while summ in nums:
            summ+=1
        return summ


            

            



        