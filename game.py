from objects import Board
from objects import HumanPlayer
from objects import ComputerPlayer
from pyfiglet import Figlet
from time import sleep


class Game:
    def __init__(self):
        self.running = True
        self.board = Board()
        self.human = HumanPlayer("O")
        self.computer = ComputerPlayer("X")
        self.winner = None

    def welcome(self):
        ttt_font = Figlet(font='big')
        print(''' 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / _
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
        ''')
        print(ttt_font.renderText(' TIC TAC TOE') , end="")
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

    def declare_victory(self):
        print(f"{self.winner} won!")
        sleep(3)

    def run(self):
        # display
        #self.board.display()
        if "X" not in self.board.fields:
            self.board.display()
            print("Computer's sign: 'X'")
            print("Your sign: 'O'")
            print()
            self.computer.first_move()
        else:
            self.computer.choose_move(self.board)
        self.board.update(self.computer.move, self.computer.sign)
        self.board.display()
        (self.victory, self.winner) = self.board.check_victory(self.computer.sign)
        #self.victory, self.winning = result[0], result[1]
        if self.victory:
            self.declare_victory()
            self.running = False
        if self.running == True:
            self.human.choose_move(self.board)
            self.board.update(self.human.move, self.human.sign)
            self.board.display()
            (self.victory, self.winner) = self.board.check_victory(self.human.sign)
            if self.victory:
                self.declare_victory()
                self.running = False

        
            





# internal tests #

def main():
    game = Game()
    game.welcome()

if __name__ == "__main__":
    main()