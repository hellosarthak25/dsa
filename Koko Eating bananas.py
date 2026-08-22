class Solution:
    def total(self, a:List[int], n:int, speed:int)->int:
        hrs=0

        for i in range(n):
            hrs += a[i] // speed

            if a[i] % speed != 0:
                hrs += 1

        return hrs

    def minEatingSpeed(self, piles:List[int], h:int)->int:
        n=len(piles)

        low=1
        high=max(piles)
        res=-1

        while(low<=high):
            guess=(low+high)//2

            hour=self.total(piles,n,guess)

            if(hour>h):
                low=guess+1
            else:
                res=guess
                high=guess-1

        return res
import math

class Solution:
    def minEatingSpeed(self, piles:List[int], h:int)->int:
        n=len(piles)

        low=1
        high=max(piles)
        res=-1

        while(low<=high):
            guess=(low+high)//2

            hour=0

            for i in range(n):
                hour += math.ceil(piles[i]/guess)

            if(hour>h):
                low=guess+1
            else:
                res=guess
                high=guess-1

        return res