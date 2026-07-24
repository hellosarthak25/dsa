class Solution:
    def minWindow(self, s: str, t: str) -> str:
        low=0
        high=0
        f={} #hashmap defined
        for ch in t:
            if ch in f:
                f[ch]+=1
            else:
                f[ch]=1 #stored the frequency(needed)
        req=len(t)
        start=0
        min_len=float('inf')
        for high in range(len(s)):
            if s[high] in f:
                if f[s[high]]>0:
                    req-=1
                f[s[high]]-=1
                while(req==0):
                    length=high-low+1
                    if length<min_len:
                        min_len=length
                        start=low
                    if s[low] in f:
                        f[s[low]]+=1
                        if f[s[low]]>0:
                            req+=1
                    low+=1
        if min_len==float('inf'):
                return ""
        return s[start:start +min_len]
        


        