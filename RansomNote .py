class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r={}
        m={}
        for ch in ransomNote:
            if ch in r:
                r[ch]+=1
            else:
                r[ch]=1
        for ch in magazine:
            if ch in m:
                m[ch]+=1
            else:
                m[ch]=1
        for ch in r:
            if ch not in m or r[ch]>m[ch]:
                return False
        return True

        