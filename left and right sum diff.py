class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=0
        total=sum(nums)
        answer=[0]*n
        for i in range(0,n):
            if (i==0):
                right=total-nums[i]
                left=0
            else:
                left+=nums[i-1]
                right=total-left-nums[i]
            answer[i]=abs(left-right)
        return answer


        