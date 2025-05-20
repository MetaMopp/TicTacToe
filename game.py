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
        self.draw = None

    def welcome(self):
        ttt_font = Figlet(font='big')
        print(''' 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ 
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \ 
\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / 
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ 
        ''')
        sleep(1)
        print(ttt_font.renderText('TIC TAC TOE') , end="")
        sleep(1.2)
        print('''
                ||================================||
                ||<> < metamopp[at]gmail.com > <> ||           
                ||================================||
        ''')
        sleep(1)
        print('''
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ 
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \ 
\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / 
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/  
        ''')
        sleep(.5)

    def explain(self):
        print()
        print('''
                      ~> Computer's sign: X <~
                      ~~>   Your sign: O   <~~
              ''')
        sleep(2.5)
        print()

    def declare_victory(self):
        print(f"                           {self.winner} won!")
        sleep(1)

    def declare_draw(self):
        print('''
                               Draw!
              ''')
        sleep(1)

    def run(self):
        # start condition
        if "X" not in self.board.fields:
            self.explain()
            print('''                    
                            Good  Luck!
                  ''')
            self.board.display()
            print()
            
            self.computer.first_move()
        else:
            self.computer.choose_move(self.board)
        # computer player
        self.board.update(self.computer.move, self.computer.sign)
        #print()
        
        self.board.display()
        #print()
        #sleep(.5)
        #print()
        (self.victory, self.winner) = self.board.check_victory(self.computer.sign)
        self.draw = self.board.check_draw(self)
        if self.draw:
            self.running = False
            self.declare_draw()
        if self.victory:
            self.declare_victory()
            self.running = False
        # human player
        if self.running == True:
            self.human.choose_move(self.board)
            self.board.update(self.human.move, self.human.sign)
            #print()
            self.board.display()
            #print()
            #sleep(.5)
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