from board import Board

class GameLogic:
    def __init__(self):
        self.board = Board()
        self.player_row = 0
        self.player_col = 0
        self.cpu_row = 0
        self.cpu_col = 0
        self.board_size = 9 

    def showBoard(self):
        self.board.show_board()

    def isPlayerWin(self):

        return self.checkWin(self.player_row, self.player_col, 'Black')

    def isCpuWin(self):

        return self.checkWin(self.cpu_row, self.cpu_col, 'White')

    def checkWin(self, row, col, color):

        directions = [(0, 1), (1, 0), (1, 1), (1, -1)] 
        for dr, dc in directions:
            count = 1
            for i in range(1, 5):
                if 0 <= row + i * dr < self.board_size and 0 <= col + i * dc < self.board_size:
                    if (color == 'Black' and self.board.isBlack(row + i * dr, col + i * dc)) or \
                       (color == 'White' and self.board.isWhite(row + i * dr, col + i * dc)):
                        count += 1
                    else:
                        break
                else:
                    break
            for i in range(-1, -5, -1):
                if 0 <= row + i * dr < self.board_size and 0 <= col + i * dc < self.board_size:
                    if (color == 'Black' and self.board.isBlack(row + i * dr, col + i * dc)) or \
                       (color == 'White' and self.board.isWhite(row + i * dr, col + i * dc)):
                        count += 1
                    else:
                        break
                else:
                    break
            if count >= 5:
                return True
        return False

    def playerRound(self):
        while True:
            try:
                player_input = input('Enter your move (row, col): ').strip()
                self.player_row, self.player_col = map(int, player_input.split())
                self.player_row -= 1 
                self.player_col -= 1  

                if (0 <= self.player_row < self.board_size and
                        0 <= self.player_col < self.board_size and
                        self.board.isempty(self.player_row, self.player_col)):
                    self.board.down(self.player_row, self.player_col, True)
                    break
                else:
                    print("Error: Invalid move, Enter again")
            except (ValueError, IndexError):
                print("Error: Invalid move, Enter again")

    def computerRound(self):
        best_row = best_col = -1
        max_continue_count = 0
        can_block_win = False

        for dir in [-1, 1]:
            if self.player_col + dir * 2 >= 0 and self.player_col + dir * 2 < self.board_size:
                if self.board.isBlack(self.player_row, self.player_col + dir) and \
                self.board.isBlack(self.player_row, self.player_col + dir * 2) and \
                self.board.isempty(self.player_row, self.player_col + dir * 3):
                    best_row = self.player_row
                    best_col = self.player_col + dir * 3
                    can_block_win = True
            if not can_block_win:
                if best_row != -1 and best_col != -1:
                    self.cpu_row = best_row
                    self.cpu_col = best_col
                    self.board.down(self.cpu_row, self.cpu_col, False)
                else:
                    print("Computer couldn't find a valid move.")

        for direction in [-1, 1]:
            count = 0
            col = self.player_col
            while 0 <= col < self.board_size and self.board.isBlack(self.player_row, col):
                count += 1
                col += direction
            if count > max_continue_count:
                max_continue_count = count
                best_row = self.player_row
                best_col = self.player_col + direction * (count + 1) 

        for direction in [-1, 1]:
            count = 0
            row = self.player_row
            while 0 <= row < self.board_size and self.board.isBlack(row, self.player_col):
                count += 1
                row += direction
            if count > max_continue_count:
                max_continue_count = count
                best_row = self.player_row + direction * (count + 1) 

        if 0 <= best_row < self.board_size and 0 <= best_col < self.board_size and self.board.isempty(best_row, best_col):
            self.cpu_row = best_row
            self.cpu_col = best_col
            self.board.down(self.cpu_row, self.cpu_col, False)
        else:
            print("Computer couldn't find a valid move.")
