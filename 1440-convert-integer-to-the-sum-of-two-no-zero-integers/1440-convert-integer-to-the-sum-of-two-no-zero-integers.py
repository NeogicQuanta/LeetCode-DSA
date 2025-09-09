class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def checkZero(n):
            if (n < 9):
                return True
            flag = 1
            while n:
                flag = n%10
                print(n, flag)
                if not flag:
                    # print("Returning False")
                    return False
                n = n//10
            
            # print("Returning True")
            return True
        
        for i in range(1,n//2+1):
            j = n - i
            if checkZero(i):
                if checkZero(j):
                    return [i,j]
            
            


