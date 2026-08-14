class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        i = 0
        j = 0
        f = {}
        ans = 0
        n = len(s)

        while j < n:
            if s[j] in f:
                f[s[j]] += 1
            else:
                f[s[j]] = 1

            while f[s[j]] > 2:
                f[s[i]] -= 1
                i += 1

            ans = max(ans, j - i + 1)
            j += 1

        return ans