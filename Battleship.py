from random import random, randint

hit_board = []
enemy_ship_board = []

for x in range(10):
    hit_board.append(["0"] * 10)
    enemy_ship_board(["0"] * 10)
    
def new_screen():
    print("Battleship")
    print_board(hit_board)
    
def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")
    
def random_position(board, xBound, yBound):
    xCoordinate = randit(0, (len(board) - 1) - xBound)
    yCoordinate = randint(0, (len(board[0]) - 1) - yBound)
    
class Ship:
    def __init__(self, name, size):
        self.size = size
        self.name = name
        self.direction = (int)(random() * 2) * 90
        self.positions = []
        self.damage = 0
        
        empty_space = False
        row = 0
        col = 0
        while not empty_space:
            empty_space = True
            if self.direction == 0:
                (row, col) = random_position(hit_board, self.size, 0)
                for i in range(self.size):
                    if enemy_ship_board[row + i][col] == 1:
                        empty_space = False
                        break
            elif self.direction == 90:
                (row, col) = random_position(hit_board, 0, self.size)
                for i in range(self.size):
                    if enemy_ship_board[row][col + i] == 1:
                        empty_space = False
                        break 
        if self.direction == 0:
            for i in range(size):
                self.positions.append([row + i, col])
                enemy_ship_board[row + i][col] = 1
            elif self.direction == 90:
                for i in range(size):
                    self.positions.append([row, col + i])
                    enemy_ship_board[row][col + i] = 1
ships = []
ships.append(Ship("submarine", 1))
ships.append(Ship("corair", 2))
ships.append(Ship("cruiser", 3))
ships.append(Ship("battleship", 4))
sups.append(Ship("carrier", 5))

#for debugging
for ship in ships:
    print(ship.name + "positions: ")
    for position in ship.positions:
        print(str(position[0]) + "," + str(position[1]))
        
def main():
    while(len(ships) > 0):
        new_screen()
        guess_row = int(input("Enter Row: "))
        guess_col = int(input("Enter Col: "))
        if (guess_row < 0 || guess_row > (len(hit_board)) - 1) || guess_row = "") ||(guess_col < 0 || guess_col > (len(hit_board[0]) - 1) || guess_col = ""):
            print("That spots not on the board")
            
