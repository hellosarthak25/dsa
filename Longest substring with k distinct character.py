class Solution:
    def longestKSubstr(self, s, k):
        low=0
        high=0
        n=len(s)
        f={}
        length=0
        res=-1
        for high in range(n):
            if s[high] not in f:
                 f[s[high]] = 0
            f[s[high]] += 1
            while len(f)>k:
                f[s[low]]-=1
                if f[s[low]]==0:
                    del f[s[low]]
                low+=1
            if len(f)==k:
                length=high-low+1
                res=max(res,length)
        return res
        