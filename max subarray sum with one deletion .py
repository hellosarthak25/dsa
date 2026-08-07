class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n=len(arr)
        onedlt=0
        nodlt=arr[0]
        res=arr[0]
        for i in range(1,n):
            prevonedlt=onedlt
            prevnodlt=nodlt
            nodlt=max(nodlt+arr[i],arr[i])
            onedlt=max(prevonedlt+arr[i],prevnodlt)
            res=max(res,max(onedlt,nodlt))
        return res


        