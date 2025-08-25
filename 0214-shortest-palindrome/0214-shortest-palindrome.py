class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0 or n == 1:
            return s
        # i, j = 0, n
        # while i == j:

        for i in range(n-1, -1, -1):
            if s[:i+1] == s[i::-1]:
                return s[i+1:][::-1] + s
