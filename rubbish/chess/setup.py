from GameLogic import GameLogic

game = GameLogic()
while True:
    game.showBoard()
    game.playerRound()
    if game.isPlayerWin():
        print('Player wins!')
        break
    game.computerRound()
    if game.isCpuWin():
        print('Computer wins!')
        break