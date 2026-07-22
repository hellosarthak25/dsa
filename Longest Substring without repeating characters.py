class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low=0
        high=0
        f={}
        res=0
        length=0
        n=len(s)
        for high in range(n):
            if s[high] not in f:
                f[s[high]]=0
            f[s[high]]+=1
            while f[s[high]]>1:
                f[s[low]]-=1 
                if f[s[low]]==0:
                    del f[s[low]]      
                low+=1
            length=high-low+1
            res=max(res,length)
        return res
        