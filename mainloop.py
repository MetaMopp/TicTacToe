from game import Game
from time import sleep



game = Game()
game.welcome()

# MAINLOOP #
while game.running:
    game.run()

    if game.running == False:
        sleep(2)
        choice = input("You you want to start a new Game? y/n ")
        if choice == "n":
            exit()
        else:
            game.running == True

