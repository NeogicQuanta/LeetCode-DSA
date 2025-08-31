class Solution:
    def findNthDigit(self, n: int) -> int:
        if n ==1:
            return 1
        count = 1
        # l = len(str(n))
        # for i in range(1, l):
        #     count += i*(10**i - 10**(i-1))
        #     print(i, count)
        # # Reached the Base Point
        i = 0
        while count < n:
            count += int(i*(10**i - 10**(i-1)))
            i += 1
            print(" ", i, count)
        i -= 1
        count -= i*(10**i - 10**(i-1))
        number = 10**(i-1)
        print("\t",i, count, number)
        temp = n - count
        print(temp)
        number += (temp)//i
        count += i*(temp//i)
        print(number, count)



        number = str(number)
        for j in number:
            if count == n:
                return int(j)
            count += 1