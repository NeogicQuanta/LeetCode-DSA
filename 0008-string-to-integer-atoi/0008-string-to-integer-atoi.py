class Solution:
    def myAtoi(self, s: str) -> int:
        if not s: return 0
        num = 0
        i = 0
        flag = 1
        while i < len(s) and s[i] == ' ': i += 1
        if i < len(s) and s[i] == '-':
            flag = -1
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1
        
        while i < len(s) and ord(s[i]) < 58 and ord(s[i]) > 47:
            num *= 10
            num += ord(s[i]) - 48
            i += 1
        num *= flag
        if flag+1 and num > 2**31 -1:
            return 2**31 -1
        elif flag == -1 and num < -2**31:
            return -2**31

        return num