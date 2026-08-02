class Solution:
    def factorial(self, n: int) -> int:
        fact=1
        i=1
        while(i<n+1):
            fact=fact*i
            i+=1
        return fact
        