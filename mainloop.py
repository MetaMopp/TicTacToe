from game import Game
from time import sleep



game = Game()
game.welcome()

# MAINLOOP #
while game.running:
    game.run()

    if game.running == False:
        print("running: ",game.running)
        sleep(3)
        choice = input("You you want to start a new Game? y/n ")
        if choice != "y":
            exit()
        else:
            game.running == True

