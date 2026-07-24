class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        low = 0
        f = [0] * 26
        n = len(s)
        res = 0

        for high in range(n):

            f[ord(s[high]) - ord('A')] += 1

            length = high - low + 1
            max_cnt = max(f)
            diff = length - max_cnt

            while diff > k:
                f[ord(s[low]) - ord('A')] -= 1
                low += 1

                length = high - low + 1
                max_cnt = max(f)
                diff = length - max_cnt

            res = max(res, length)

        return res