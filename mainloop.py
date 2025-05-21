from game import Game
from time import sleep


game = Game()
game.welcome()

# MAINLOOP #
while game.running:
    game.run()

    if game.running == False:
        sleep(1)
        choice = input('''                   
                   Do you want to start a new Game? 
                               y/n: ''')
        if choice == "y":
            game.running = True
            sleep(1)
            game.board.fields = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            print('''     
                         ~~~~~~~~~~~~~~~~~                
                           Welcome back!
                  ''')
        elif choice == "n":
            exit()


