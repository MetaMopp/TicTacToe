from game import Game
from time import sleep
from pyfiglet import Figlet

ttt_font = Figlet(font='big')


print(''' 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / _
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 ''')
print(ttt_font.renderText('TIC TAC TOE') , end="")

print('''
                ||================================||
                ||<> < metamopp[at]gmail.com > <> ||           
                ||================================||
''')

print('''
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / _
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
''')

game = Game()
game.welcome()

# MAINLOOP #
while game.running:
    game.run()

if game.running == False:
    print(game.board.victory_message)
    sleep(3)
    print("You you want to start a new Game?")
