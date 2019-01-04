import random

class Maze:
    
    def __init__(self, maze):
        self.maze = maze
        self.unsolved = True

    def CanMove(self, row, col):
        if 0 <= row < len(self.maze) and 0 <= col < len(self.maze[row]):
            return self.maze[row][col] == "X" or self.maze[row][col] == "E"

    def Move(self, row, col):
        if self.unsolved:
            if self.maze[row][col] == "E":
                self.unsolved = False
            elif self.maze[row][col] != "S":
                self.maze[row][col] = 'P' 
            
            # up
            if ( self.CanMove(row-1, col) ):
                self.Move(row-1, col)
                if self.unsolved:
                    self.maze[row-1][col] = 'D'

            # right
            if ( self.CanMove(row, col + 1) ):
                self.Move(row, col + 1)
                if self.unsolved:
                    self.maze[row][col+1] = 'D'
            # down
            if ( self.CanMove(row + 1, col) ):
                self.Move(row + 1, col)
                if self.unsolved:
                    self.maze[row + 1][col] = 'D'

            # Left
            if ( self.CanMove(row, col-1) ):
                self.Move(row, col-1)
                if self.unsolved:
                    self.maze[row][col-1] = 'D'

    def Print(self):
        for line in self.maze:
            for letter in line:
                print(letter, end='')
            print()
        print()

    def FindStart(self):
        for row, line in enumerate(self.maze):
            endColumn = line.index("S")
            if endColumn >= 0:
                return row, endColumn
    
    def Solve(self):
        startRow, startCol = self.FindStart()
        self.Move( startRow, startCol )


#mazeFile = open("Maze1.txt")
#maze = mazeFile.readlines()
#twoDMaze = []
#for index in range(len(maze)):
#    twoDMaze.append([])
#    for letter in maze[index]:
#        twoDMaze[index].append(letter)

#firstMaze = Maze(twoDMaze)
#print("Starting maze:")
#print()
#firstMaze.Print()
#firstMaze.Sovle()
#print()
#print("Ending maze:")
#print()
#firstMaze.Print()
#print()

for mazeNumber in range(1000):
    mazeList = []
    for row in range(10):
        mazeList.append([])
        for col in range(10):
            if random.randint(0,1) == 0:
                mazeList[row].append("X")
            else:
                mazeList[row].append("W")

    mazeList[0][0] = 'S'
    mazeList[9][9] = 'E'

    newMaze = Maze(mazeList)
    newMaze.Solve()
    if not newMaze.unsolved:
        print("Maze Number:", mazeNumber)
        newMaze.Print()
        print()