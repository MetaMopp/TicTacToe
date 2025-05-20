from objects import Board
from objects import HumanPlayer
from objects import ComputerPlayer
from pyfiglet import Figlet


class Game:
    def __init__(self):
        self.running = True
        self.board = Board()
        self.human = HumanPlayer("O")
        self.computer = ComputerPlayer("X")

    def welcome(self):
        ttt_font = Figlet(font='big')
        print(''' 
        / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
       / /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
       \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / _
        \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
        ''')
        print(ttt_font.renderText('        TIC TAC TOE') , end="")
        print('''
                        ||================================||
                        ||<> < metamopp[at]gmail.com > <> ||           
                        ||================================||
        ''')
        print('''
        / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
       / /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
       \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / _
        \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
        ''')

    def run(self):
        # display
        self.board.display()
        if "X" not in self.board.fields:
            self.computer.first_move()
        else:
            self.computer.choose_move(self.board)
        self.board.update(self.computer.move, self.computer.sign)
        self.board.display()
        self.board.check_victory()
        self.human.choose_move(self.board)
        self.board.update(self.human.move, self.human.sign)
        self.board.display()




# internal tests #

def main():
    game = Game()
    game.welcome()

if __name__ == "__main__":
    main()