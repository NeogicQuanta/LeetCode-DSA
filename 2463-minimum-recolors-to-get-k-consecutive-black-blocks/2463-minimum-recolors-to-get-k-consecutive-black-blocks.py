class Solution:
    def minimumRecolors(self, s: str, k: int) -> int:
        data = {"W":0, "B":0}
        for i in range(k):
            data[s[i]] += 1
        
        minw = data["W"]

        for i in range(k,len(s)):
            data[s[i]] += 1
            data[s[i-k]] -= 1
            if data["W"] < minw:
                minw = data["W"]
        return minw