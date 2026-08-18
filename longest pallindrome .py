class Solution:
    def longestPalindrome(self, s: str) -> int:
        f={}
        for ch in s:
            if ch in f:
                f[ch]+=1
            else:
                f[ch]=1

        odd=False
        res=0

        for ch in f:
            if f[ch]%2==0:
                res+=f[ch]
            else:
                odd=True
                res+=f[ch]-1

        if odd:
            res+=1

        return res
