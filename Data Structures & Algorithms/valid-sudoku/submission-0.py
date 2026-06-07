class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if (self.checkColums(board) and self.checkRows(board) and self.checkBoxes(board)):
            return True
        
        return False
    
    def checkColums(self, board: list[list[str]]) -> bool:
        colDict = {}
        for x in range(len(board)):
            for j in range(len(board)):
                if board[j][x] == ".":
                    continue
                elif colDict.get(board[j][x]):
                    return False
                else:
                    colDict.setdefault(board[j][x], 1)
            colDict.clear()
        return True
    
    def checkRows(self, board: list[list[str]]) -> bool:
        rowDict = {}
        for x in range(len(board)):
            for j in range(len(board)):
                if board[x][j] == ".":
                    continue
                elif rowDict.get(board[x][j]):
                    return False
                else:
                    rowDict.setdefault(board[x][j], 1)
            rowDict.clear()
        return True

    def checkBoxes(self, board: list[list[str]]) -> bool:
        incX = 0
        incY = 0
        incXmax = 3
        incYmax = 3
        count = 0
        result = True

        while (count < 3):
            boxDict = {}
            for i in range(3):
                for x in range(incX, incXmax):
                    for j in range(incY, incYmax):
                        if board[x][j] == ".":
                            continue
                        elif boxDict.get(board[x][j]):
                            result = False
                            break
                        else:
                            boxDict.setdefault(board[x][j], 1)
                incY += 3
                incYmax += 3
                boxDict.clear()
            incX += 3
            incXmax += 3
            incY = 0
            incYmax = 3
            count += 1

        return result