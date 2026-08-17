class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        f={}
        for ch in text:
            if ch in f:
                f[ch]+=1
            else:
                f[ch]=1
        b = f.get('b',0)
        a = f.get('a',0)
        l = f.get('l',0)//2
        o = f.get('o',0)//2
        n = f.get('n',0)
        return min(b,a,l,o,n)
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        f = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        for ch in text:
            if ch in f:
                f[ch] += 1

        f['l'] //= 2
        f['o'] //= 2

        return min(f['b'], f['a'], f['l'], f['o'], f['n'])