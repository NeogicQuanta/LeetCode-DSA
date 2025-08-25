num = [[1,2,3], [4,5,6], [7,8,9]]
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        v = len(mat)
        h = len(mat[0])
        if v == 1 and h == 1:
            return [mat[0][0]]
        if v == 1:
            return mat[0]
        if h == 1:
            return [ i[0] for i in mat]
        ans = []
        flag = True
        i , j = 0 , 0
        while i != v and j != h:
            if flag:
                while i >= 0 and j != h:
                    print(mat[i][j], i, j)
                    ans.append(mat[i][j])
                    i -= 1
                    j += 1
                flag = not flag
                if j == h:
                    i += 1
                    j = h-1
                    
                i += 1

            else:
                while j >= 0 and i != v:
                    print(mat[i][j], i, j)
                    ans.append(mat[i][j])
                    j -= 1
                    i += 1
                flag = not flag
                if i == v:
                    j += 1
                    i = v-1
                
                j += 1
        return ans
