class Solution:
    def reverse(self, x: int) -> int:
        i = 0
        flag = 1
        count = 0
        if x< 0: flag = -1; x *= -1
        while x:
            i *= 10
            i += x%10
            x = x//10
            count += 1
            if count > 32: return 0
            
        if i < -2**31 or i > 2**31 -1: return 0
        
        return i*flag