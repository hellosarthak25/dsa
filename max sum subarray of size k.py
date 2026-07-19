class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        sum=0
        res=0
        low=0
        high=k-1
        for i in range(low,high+1):
            sum=sum+arr[i]
        while(high<len(arr)):
            res=max(res,sum)
            low+=1
            high+=1
            if(high==len(arr)):
                break
            sum=sum-arr[low-1]+arr[high]
        return res