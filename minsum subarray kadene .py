class Solution:
    def smallestSumSubarray(self, A, N):
        bestending=A[0]
        ans=A[0]
        for i in range(1,N):
            v1=bestending+A[i]
            v2=A[i]
            bestending=min(v1,v2)
            ans=min(bestending , ans)
        return ans
        
        
