from random import randint 
from time import sleep

class Board:
    def __init__(self):
        self.fields = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def display(self):
        # first row
        print("+-----------+")
        print("| ", end="")
        for self.field in self.fields[:3]:
            print(self.field, end=" | ")
        print()
        # second row
        print("+-----------+")
        print("| ", end="")
        for self.field in self.fields[3:6]:
            print(self.field, end=" | ")
        print()
        # third row
        print("+-----------+")
        print("| ", end="")
        for self.field in self.fields[6:]:
            print(self.field, end=" | ")
        print()
        print("+-----------+")


    def update(self, move, sign):
        self.fields[move-1] = sign

    def check_field(self, move):
        if move in self.fields:
            self.free = True
        else:
            self.free = False
        return self.free

    def check_victory(self, sign):
        victory = False
        if self.fields[0] == sign and self.fields[1] == sign and self.fields[2] == sign\
        or self.fields[3] == sign and self.fields[4] == sign and self.fields[5] == sign\
        or self.fields[6] == sign and self.fields[7] == sign and self.fields[8] == sign\
        or self.fields[0] == sign and self.fields[3] == sign and self.fields[6] == sign\
        or self.fields[1] == sign and self.fields[4] == sign and self.fields[7] == sign\
        or self.fields[2] == sign and self.fields[5] == sign and self.fields[8] == sign\
        or self.fields[0] == sign and self.fields[4] == sign and self.fields[8] == sign\
        or self.fields[2] == sign and self.fields[4] == sign and self.fields[6] == sign:
            victory = True
            if sign == "X":
                winner = "Computer"
            else:
                winner = "You"
            return victory, winner
        else:
            winner = None
            return victory, winner

# basic class 
class Player:
    def __init__(self, sign):
        self.sign = sign


class HumanPlayer(Player):
    def __init__(self, sign):
        super().__init__(sign)

    def choose_move(self, board):
        while True:
            try:
                self.move = int(input("Enter your move: ")) 
                if self.move > 0 and self.move < 10:
                    free = board.check_field(self.move)
                    if free:
                        break
                    else: 
                        print("Try again...")
            except ValueError:
                print("Input must be a free Integer within the field's range 1 - 9.")
    

class ComputerPlayer(Player):
    def __init__(self, sign):
        super().__init__(sign)

    def first_move(self):
        print("Computer's turn: ")
        self.move = 5

    def choose_move(self, board):
        print("Computer's turn: ")
        while True:
            self.move = randint(0, 10)
            if self.move > 0 and self.move < 10:
                    free = board.check_field(self.move)
                    if free:
                        break


# internal tests #

def main():
    board = Board()
    human = HumanPlayer("O")
    computer = ComputerPlayer("X")

    board.display()
    sleep(2)

    computer.first_move()
    board.update(computer.move, computer.sign)
    board.display()
    sleep(2)
    board.check_victory()

    human.choose_move(board)
    board.update(human.move, human.sign)
    board.display()
    sleep(2)
    board.check_victory()

    computer.choose_move(board)
    board.update(computer.move, computer.sign)
    board.display()
    sleep(2)
    board.check_victory()



if __name__ == "__main__":
    main()