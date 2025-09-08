class Solution:
    def maxFreqSum(self, s: str) -> int:
        def isVowel(s):
            a = set("aeiou")
            if s in a:
                return True 
            return False
        
        dict1 = {}
        dict2 = {}

        v = 0
        c = 0
        for i in s:
            if isVowel(i):
                if i in dict1:
                    dict1[i] +=1
                else:
                    dict1[i] = 1
                if dict1[i] > v:
                    v = dict1[i]
            else:
                if i in dict2:
                    dict2[i] +=1
                else:
                    dict2[i] = 1
                if dict2[i] > c:
                    c = dict2[i]
        m = c + v
        return m
            