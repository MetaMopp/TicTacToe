from game import Game
from time import sleep

game = Game()

# MAINLOOP #
while game.running:
    game.run()

if game.running == False:
    print(game.board.victory_message)
    sleep(3)
    print("You you want to start a new Game?")
    