import os 

class Board:
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    def show_board(self):
        os.system('cls')
        print('  1  2  3  4  5  6  7  8  9 ')
        for r in range(0, len(self.board)):
            data = str(r + 1)
            for c in range(0, len(self.board[r])):
                if self.board[r][c] == 0:
                    data += ' + '
                elif self.board[r][c] == 1:
                    data += ' □ '
                else:
                    data += ' ▲ '
            print(data)

    def isempty(self, row, col):
        return self.board[row][col] == 0  

    def down(self, row, col, isPlayer):
        self.board[row][col] = 2 if isPlayer else 1 


    def isBlack(self, row, col):
        return self.board[row][col] == 2  

    def isWhite(self, row, col):
        return self.board[row][col] == 1 