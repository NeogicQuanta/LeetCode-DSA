class Solution:
    def findNthDigit(self, n: int) -> int:
        if n ==1:
            return 1
        count = 1
        i = 0
        while count < n:
            count += int(i*(10**i - 10**(i-1)))
            i += 1
        i -= 1
        count -= i*(10**i - 10**(i-1))
        
        number = 10**(i-1)
        temp = n - count
        number += (temp)//i
        count += i*(temp//i)

        number = str(number)
        for j in number:
            if count == n:
                return int(j)
            count += 1