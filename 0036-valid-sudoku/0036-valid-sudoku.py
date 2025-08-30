class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        a = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        b = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        c = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in a[i]:
                    return False
                a[i].add(board[i][j])

                if board[i][j] in b[j]:
                    return False
                b[j].add(board[i][j])

                if board[i][j] in c[(i//3)*3 + (j//3)]:
                    return False
                c[(i//3)*3 + (j//3)].add(board[i][j])
        return True