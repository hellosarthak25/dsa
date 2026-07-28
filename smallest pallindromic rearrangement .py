class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)
        mid=n//2
        first="".join(sorted(s[:mid]))
        if n%2!=0:
            middle=s[mid]
        else:
            middle=""
        return first + middle + first[::-1]

        