import os
import copy #For the deep copying to calculate the number of jumps possible for each move
import unittest
import array
class Checkered:
    WHITE = 'W'
    BLACK = 'B'
    SPACE = ' '
    board = [[]]
    kingRow = 0
    kingCol = 0
    def __init__(self, num_white_checker, num_black_cheker, test_cases):
        self.num_white_checker = 0
        self.num_black_cheker = 0
        self.test_cases = 0
        self.total_white = num_white_checker
        self.total_black = num_black_cheker
        self.num_of_spaces = 8
        for row in range(self.num_of_spaces):
            self.board.append([])
            for col in range(self.num_of_spaces):
                self.board[row].append(Checkered.SPACE)


    def print_board(self):
        for row in self.board:
            if not row: break
            print('-' * (17))
            print('|', end="")
            for character in row:
                print( character, end='|')
            print()
        print()
        print(' ' * (17))

    def Reset(self):
        for i in range(self.num_of_spaces):
            for j in range(self.num_of_spaces):
                self.board[i][j] = self.SPACE
        self.print_board()

    def addChecker(self, row, col):
        self.row = 0
        self.col = 0
        filename = input('Enter a filename: ') #Reading the file
        f = open( filename, 'r')
        while True:
            line = f.readline().rstrip()
            if not line:
                    break
            self.test_cases = int(line)
            for i in range(0, self.test_cases):
                line = f.readline()
                if not line:
                    break
                ar = [int(k) for k in line.split(' ')] #Had to use the split to separate the space
                self.num_white_checker = ar[0]
                self.num_black_checker = ar[1]
                for w in range(0, int(self.num_white_checker)):
                    line = f.readline()
                    ar = [int(k) for k in line.split(' ')]
                    ii = int(ar[0])
                    jj = int(ar[1])
                    self.board[ii][jj] = 'W'
                    if (w == 0):
                        self.kingRow = ar[0]
                        self.kingCol = ar[1]
                for b in range(0, int(self.num_black_checker)):
                    line = f.readline().rstrip()
                    ar = [int(k) for k in line.split(' ')]
                    ii = int(ar[0])
                    jj = int(ar[1])
                    self.board[ii][jj] = 'B'
                self.print_board() #I printed the board to make it easier for you to check :) even though it doesnt say that in the assignment guide
                maxNJ = 0
                nj = 0
                maxNJ = self.CheckAllDirs(self.kingRow, self.kingCol, nj, maxNJ)
                print("The number of jumps is %d" % maxNJ)
                os.system("pause")

    def CheckAllDirs(self, row, col, nj, maxNJ): #This is where the recursion magic happens
        if self.num_white_checker > 0 and 0 <= row < self.num_of_spaces and 0 <= col < self.num_of_spaces:
            if self.isDownRight(row, col):
                maxNJ = self.CheckAllDirs(row+2, col+2, nj+1, maxNJ)
            if self.isDownLeft(row, col):
                maxNJ = self.CheckAllDirs(row+2, col-2, nj+1, maxNJ)
            if self.isUpRight(row, col):
                maxNJ = self.CheckAllDirs(row-2, col+2, nj+1, maxNJ)
            if self.isUpLeft(row, col):
                maxNJ = self.CheckAllDirs(row-2, col-2, nj+1, maxNJ)
            if maxNJ < nj:
                maxNJ = nj
        return maxNJ

    def isDownRight(self, row, col):#To make sure it is ok to move in this specific direction
        row += 1
        col += 1
        if 1 <= row < self.num_of_spaces - 1 and 1 <= col < self.num_of_spaces - 1:
            if self.board[row][col] == Checkered.BLACK and self.board[row+1][col+1] == Checkered.SPACE:
                self.board[row][col] = Checkered.SPACE
                return True
        return False

    def isDownLeft(self, row, col):#To make sure it is ok to move in this specific direction
        row += 1
        col -= 1
        if 1 <= row < self.num_of_spaces - 1 and 1 <= col < self.num_of_spaces - 1:
            if self.board[row][col] == Checkered.BLACK and self.board[row+1][col-1] == Checkered.SPACE:
                self.board[row][col] = Checkered.SPACE
                return True
        return False

    def isUpRight(self, row, col):#To make sure it is ok to move in this specific direction
        row -= 1
        col += 1
        if 1 <= row < self.num_of_spaces - 1 and 1 <= col < self.num_of_spaces - 1:
            if self.board[row][col] == Checkered.BLACK and self.board[row-1][col+1] == Checkered.SPACE:
                self.board[row][col] = Checkered.SPACE
                return True
        return False

    def isUpLeft(self, row, col):#To make sure it is ok to move in this specific direction
        row -= 1
        col -= 1
        if 1 <= row < self.num_of_spaces - 1 and 1 <= col < self.num_of_spaces - 1:
            if self.board[row][col] == Checkered.BLACK and self.board[row-1][col-1] == Checkered.SPACE:
                self.board[row][col] = Checkered.SPACE
                return True
        return False
            

def main():
    ch = Checkered(0,0,0)
    ch.addChecker(0, 0)

if __name__ == '__main__':
    main()

class Testing(unittest.TestCase):

    def test_split(self): #Would have done more tests but felt the 17 input files were more than helpful to test validity of code
        s = str('3 3')
        self.assertEqual(s.split(), ['3', '3'])
        with self.assertRaises(TypeError):
=======
import os
import copy #For the deep copying to calculate the number of jumps possible for each move
import unittest
import array
class Checkered:
    WHITE = 'W'
    BLACK = 'B'
    SPACE = ' '
    board = [[]]
    kingRow = 0
    kingCol = 0
    def __init__(self, num_white_checker, num_black_cheker, test_cases):
        self.num_white_checker = 0
        self.num_black_cheker = 0
        self.test_cases = 0
        self.total_white = num_white_checker
        self.total_black = num_black_cheker
        self.num_of_spaces = 8
        for row in range(self.num_of_spaces):
            self.board.append([])
            for col in range(self.num_of_spaces):
                self.board[row].append(Checkered.SPACE)


    def print_board(self):
        for row in self.board:
            if not row: break
            print('-' * (17))
            print('|', end="")
            for character in row:
                print( character, end='|')
            print()
        print()
        print(' ' * (17))

    def Reset(self):
        for i in range(self.num_of_spaces):
            for j in range(self.num_of_spaces):
                self.board[i][j] = self.SPACE
        self.print_board()

    def addChecker(self, row, col):
        self.row = 0
        self.col = 0
        filename = input('Enter a filename: ') #Reading the file
        f = open( filename, 'r')
        while True:
            line = f.readline().rstrip()
            if not line:
                    break
            self.test_cases = int(line)
            for i in range(0, self.test_cases):
                line = f.readline()
                if not line:
                    break
                ar = [int(k) for k in line.split(' ')] #Had to use the split to separate the space
                self.num_white_checker = ar[0]
                self.num_black_checker = ar[1]
                for w in range(0, int(self.num_white_checker)):
                    line = f.readline()
                    ar = [int(k) for k in line.split(' ')]
                    ii = int(ar[0])
                    jj = int(ar[1])
                    self.board[ii][jj] = 'W'
                    if (w == 0):
                        self.kingRow = ar[0]
                        self.kingCol = ar[1]
                for b in range(0, int(self.num_black_checker)):
                    line = f.readline().rstrip()
                    ar = [int(k) for k in line.split(' ')]
                    ii = int(ar[0])
                    jj = int(ar[1])
                    self.board[ii][jj] = 'B'
                self.print_board() #I printed the board to make it easier for you to check :) even though it doesnt say that in the assignment guide
                maxNJ = 0
                nj = 0
                maxNJ = self.CheckAllDirs(self.kingRow, self.kingCol, nj, maxNJ)
                print("The number of jumps is %d" % maxNJ)
                os.system("pause")

    def CheckAllDirs(self, row, col, nj, maxNJ): #This is where the recursion magic happens
        if self.num_white_checker > 0 and 0 <= row < self.num_of_spaces and 0 <= col < self.num_of_spaces:
            if self.isDownRight(row, col):
                maxNJ = self.CheckAllDirs(row+2, col+2, nj+1, maxNJ)
            if self.isDownLeft(row, col):
                maxNJ = self.CheckAllDirs(row+2, col-2, nj+1, maxNJ)
            if self.isUpRight(row, col):
                maxNJ = self.CheckAllDirs(row-2, col+2, nj+1, maxNJ)
            if self.isUpLeft(row, col):
                maxNJ = self.CheckAllDirs(row-2, col-2, nj+1, maxNJ)
            if maxNJ < nj:
                maxNJ = nj
        return maxNJ

    def isDownRight(self, row, col):#To make sure it is ok to move in this specific direction
        row += 1
        col += 1
        if 1 <= row < self.num_of_spaces - 1 and 1 <= col < self.num_of_spaces - 1:
            if self.board[row][col] == Checkered.BLACK and self.board[row+1][col+1] == Checkered.SPACE:
                self.board[row][col] = Checkered.SPACE
                return True
        return False

    def isDownLeft(self, row, col):#To make sure it is ok to move in this specific direction
        row += 1
        col -= 1
        if 1 <= row < self.num_of_spaces - 1 and 1 <= col < self.num_of_spaces - 1:
            if self.board[row][col] == Checkered.BLACK and self.board[row+1][col-1] == Checkered.SPACE:
                self.board[row][col] = Checkered.SPACE
                return True
        return False

    def isUpRight(self, row, col):#To make sure it is ok to move in this specific direction
        row -= 1
        col += 1
        if 1 <= row < self.num_of_spaces - 1 and 1 <= col < self.num_of_spaces - 1:
            if self.board[row][col] == Checkered.BLACK and self.board[row-1][col+1] == Checkered.SPACE:
                self.board[row][col] = Checkered.SPACE
                return True
        return False

    def isUpLeft(self, row, col):#To make sure it is ok to move in this specific direction
        row -= 1
        col -= 1
        if 1 <= row < self.num_of_spaces - 1 and 1 <= col < self.num_of_spaces - 1:
            if self.board[row][col] == Checkered.BLACK and self.board[row-1][col-1] == Checkered.SPACE:
                self.board[row][col] = Checkered.SPACE
                return True
        return False
            

def main():
    ch = Checkered(0,0,0)
    ch.addChecker(0, 0)

if __name__ == '__main__':
    main()

class Testing(unittest.TestCase):

    def test_split(self): #Would have done more tests but felt the 17 input files were more than helpful to test validity of code
        s = str('3 3')
        self.assertEqual(s.split(), ['3', '3'])
        with self.assertRaises(TypeError):
>>>>>>> origin/master
            s.split(2)