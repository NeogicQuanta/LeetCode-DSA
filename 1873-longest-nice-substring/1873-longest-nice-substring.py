class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return ""
        d = set(s)
        for i in range(n):
            if s[i].swapcase() not in d:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                return left if len(left) >= len(right) else right
        return s