class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        f={}
        f[0]=1
        presum=0
        count=0
        for i in range (len(nums)):
            presum+=nums[i]
            remove=presum-k
            if remove in f:
                count+=f[remove]
            if presum in f:
                f[presum]+=1
            else:
                f[presum]=1
        return count


   
        