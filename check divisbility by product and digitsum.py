class Solution:
    def checkDivisibility(self, n: int) -> bool:
        product=1
        digitsum=0
        res=n
        while n>0:
            digit=n%10
            digitsum+=digit
            product=product*digit
            n=n//10
        x=digitsum+product
        if(res%x==0):
            return True
        else:
            return False

        