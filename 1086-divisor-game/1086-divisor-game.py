class Solution:
    def divisorGame(self, n: int) -> bool:
        return not bool(n&1)
