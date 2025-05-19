from objects import Board
from objects import HumanPlayer
from objects import ComputerPlayer

class Game:
    def __init__(self):
        self.running = True
        self.board = Board()
        self.human = HumanPlayer("O")
        self.computer = ComputerPlayer("X")

    def welcome(self):
        self.greet = "\U+2757 Welcome to Tic Tac Toe \U+2757"

    def run(self):
        # display
        self.board.display()
        if "X" not in self.board.fields:
            self.computer.first_move()
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