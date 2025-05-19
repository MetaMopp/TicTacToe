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

    def check_victory(self):
        if self.fields[:3] == "X" or self.fields[3:6] == "X" or self.fields[6:] == "X"\
        or self.fields[0] == "X" and self.fields[3] == "X" and self.fields[6] == "X"\
        or self.fields[1] == "X" and self.fields[4] == "X" and self.fields[7] == "X"\
        or self.fields[2] == "X" and self.fields[5] == "X" and self.fields[8] == "X"\
        or self.fields[0] == "X" and self.fields[4] == "X" and self.fields[8] == "X"\
        or self.fields[2] == "X" and self.fields[4] == "X" and self.fields[6] == "X":
            self.victory_message = "The Computer won the Game."
            self.running = False
            return self.victory_message
        elif self.fields[:3] == "O" or self.fields[3:6] == "O" or self.fields[6:] == "O"\
        or self.fields[0] == "O" and self.fields[3] == "O" and self.fields[6] == "O"\
        or self.fields[1] == "O" and self.fields[4] == "O" and self.fields[7] == "O"\
        or self.fields[2] == "O" and self.fields[5] == "O" and self.fields[8] == "O":
            self.victory_message = "You won the Game."
            self.running = False
            return self.victory_message
        else:
            pass

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