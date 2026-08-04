class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = set()
        colset = set()
        sqset = set()

        for row in range(9):
            for col in range(9):
                if board[row][col]==".":
                    continue
                if int(board[row][col]) in rowset:
                    return False
                else:
                    rowset.add(int(board[row][col]))
            rowset.clear()

        for row in range(9):
            for col in range(9):
                if board[col][row]==".":
                    continue
                if int(board[col][row]) in colset:
                    return False
                else:
                    colset.add(int(board[col][row]))
            colset.clear()

        for row_st in range(0,7,3):
            for col_st in range(0,7,3):
                for row in range(row_st,row_st+3):
                    for col in range(col_st,col_st+3):
                        if board[row][col]==".":
                            continue
                        if int(board[row][col]) in sqset:
                            return False
                        else:
                            sqset.add(int(board[row][col]))   
                sqset.clear()            

        return True