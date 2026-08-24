class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 1
        k = x // 2

        if x == 0 or x == 1:
            return x

        for i in range(1, k + 1):
            if i * i <= x:
                ans = i
            else:
                break

        return ans
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        low=1
        high=x//2
        ans=1
        while(low<=high):
            mid=(low+high)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans

        