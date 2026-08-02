class Solution:
    def isHappy(self, n: int) -> bool:
        def s(n):
            summ=0
            while(n>0):
                d=n%10
                n=n//10
                summ+=d*d
            return summ
        slow=n
        fast=n
        while(fast!=1):
            slow=s(slow)
            fast=s(fast)
            fast=s(fast)
            if(slow==fast and slow!=1):
                return False
        return True

        