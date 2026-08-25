class Solution:
    def frequencySort(self, s: str) -> str:
        f = {}
        ans = ""

        # Count frequency
        for ch in s:
            if ch in f:
                f[ch] += 1
            else:
                f[ch] = 1

        # Frequency from high to low
        for i in range(len(s), 0, -1):
            for ch in f:
                if f[ch] == i:
                    ans += ch * i

        return ans