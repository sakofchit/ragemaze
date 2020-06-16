
import pygame, sys
from pygame.locals import*

pygame.init()

screen = pygame.display.set_mode((640,480),pygame.FULLSCREEN)
pygame.display.set_caption('Rage Maze')

START = (0,255,0)
END = (255,0,0)
WALL = (0,0,255)
RUNNER = (255,102,0)
RUNNER2 = (0,206,205)

background = pygame.image.load('maze2.png')
xpos = 0
ypos = 0

def DrawBackground(background, xpos, ypos):
    screen.blit(background, [xpos, ypos])


class cell:
    def __init__(self):
        self.number = 0
        self.north = True
        self.east = True
        self.south = True
        self.west = True
#grid
row1 = [1,1,1,1,1,1,1,1,1,1,1,1]
row2 = [1,1,1,1,1,1,1,1,1,1,1,1]
row3 = [1,1,1,1,1,1,1,1,1,1,1,1]
row4 = [1,1,1,1,1,1,1,1,1,1,1,1]
row5 = [1,1,1,1,1,1,1,1,1,1,1,1]
row6 = [1,1,1,1,1,1,1,1,1,1,1,1]
row7 = [1,1,1,1,1,1,1,1,1,1,1,1]
row8 = [1,1,1,1,1,1,1,1,1,1,1,1]
row9 = [1,1,1,1,1,1,1,1,1,1,1,1]
row10 = [1,1,1,1,1,1,1,1,1,1,1,1]
row11 = [1,1,1,1,1,1,1,1,1,1,1,1]
row12 = [1,1,1,1,1,1,1,1,1,1,1,1]
row13 = [1,1,1,1,1,1,1,1,1,1,1,1]
row14 = [1,1,1,1,1,1,1,1,1,1,1,1]
row15 = [1,1,1,1,1,1,1,1,1,1,1,1]
row16 = [1,1,1,1,1,1,1,1,1,1,1,1]

grid = [row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,row12,row13,row14,row15,row16]

rows = 0
columns = 0
count = 1

while rows < 17:
    columns = 0
    while columns < 13:
        grid[rows][columns] = cell()
        grid[rows][columns].number = count
        count += 1
        columns += 1
    rows += 1


columns = 0
while columns <13:
    grid[0][columns].north = False
    columns += 1

rows = 0
while rows <17:
    grid[rows][0].west = False
    rows += 1

columns = 0
while columns <13:
    grid[16][columns].south = False
    columns += 1

rows = 0
while rows <17:
    grid[rows][12].east = False
    rows += 1



class Runner:
    def __init__(self, row, col, grid):
        self.row = row
        self.col = col
        self.grid = grid
        self.current_cell = grid[row][col]


    def move(self, newRow, newCol):
        self.row = newRow
        self.col = newCol
        self.current_cell = self.grid[newRow][newCol]

    def moveLeft(self):
        if self.current_cell.west == True:
            self.move(self.row, self.col-1)
            print self.current_cell.number
        else:
            print "Cant go left."

    def moveRight(self):
        if self.current_cell.east == True:
            self.move(self.row, self.col+1)
            print self.current_cell.number
        else:
            print "Cant go right."

    def moveUp(self):
        if self.current_cell.north == True:
            self.move(self.row-1, self.col)
            print self.current_cell.number
        else:
            print "Cant go up."

    def moveDown(self):
        if self.current_cell.south == True:
            self.move(self.row+1, self.col)
            print self.current_cell.number
        else:
            print "Cant go down."


class Runner2:
    def __init__(self, row, col, grid):
        self.row = row
        self.col = col
        self.grid = grid
        self.current_cell = grid[row][col]


    def move(self, newRow, newCol):
        self.row = newRow
        self.col = newCol
        self.current_cell = self.grid[newRow][newCol]

    def moveLeft(self):
        if self.current_cell.west == True:
            self.move(self.row, self.col-1)
            print self.current_cell.number
        else:
            print "Cant go left."

    def moveRight(self):
        if self.current_cell.east == True:
            self.move(self.row, self.col+1)
            print self.current_cell.number
        else:
            print "Cant go right."

    def moveUp(self):
        if self.current_cell.north == True:
            self.move(self.row-1, self.col)
            print self.current_cell.number
        else:
            print "Cant go up."

    def moveDown(self):
        if self.current_cell.south == True:
            self.move(self.row+1, self.col)
            print self.current_cell.number
        else:
            print "Cant go down."




#Entire Lefthand side boundaries
grid[0][0].south = False
grid[0][0].north = False
grid[0][0].west = False
grid[0][0].east = True

grid[1][0].north = False
grid[1][0].south = True
grid[1][0].west = False
grid[1][0].east = True

grid[2][0].north = True
grid[2][0].south = True
grid[2][0].west = False
grid[2][0].east = False

grid[3][0].north = True
grid[3][0].south = True
grid[3][0].west = False
grid[3][0].east = False

grid[4][0].north = True
grid[4][0].south = False
grid[4][0].west = False
grid[4][0].east = False

grid[5][0].north = False
grid[5][0].south = True
grid[5][0].west = False
grid[5][0].east = True

grid[6][0].north = True
grid[6][0].south = True
grid[6][0].west = False
grid[6][0].east = False

grid[7][0].north = True
grid[7][0].south = True
grid[7][0].west = False
grid[7][0].east = False

grid[8][0].north = True
grid[8][0].south = True
grid[8][0].west = False
grid[8][0].east = False

grid[9][0].north = True
grid[9][0].south = True
grid[9][0].west = False
grid[9][0].east = False

grid[10][0].north = True
grid[10][0].south = False
grid[10][0].west = False
grid[10][0].east = False

grid[11][0].north = False
grid[11][0].south = True
grid[11][0].west = False
grid[11][0].east = True

grid[12][0].north = True
grid[12][0].south = False
grid[12][0].west = False
grid[12][0].east = True

grid[13][0].north = False
grid[13][0].south = True
grid[13][0].west = False
grid[13][0].east = True

grid[14][0].north = True
grid[14][0].south = True
grid[14][0].west = False
grid[14][0].east = False

grid[15][0].north = True
grid[15][0].south = False
grid[15][0].west = False
grid[15][0].east = True

grid[0][1].north = False
grid[0][1].south = True
grid[0][1].west = True
grid[0][1].east = True

grid[1][1].north = True
grid[1][1].south = False
grid[1][1].west = True
grid[1][1].east = False

grid[2][1].north = False
grid[2][1].south = True
grid[2][1].west = False
grid[2][1].east = True

grid[3][1].north = True
grid[3][1].south = True
grid[3][1].west = False
grid[3][1].east = False

grid[4][1].north = True
grid[4][1].south = False
grid[4][1].west = False
grid[4][1].east = True

grid[5][1].north = False
grid[5][1].south = True
grid[5][1].west = True
grid[5][1].east = False

grid[6][1].north = True
grid[6][1].south = True
grid[6][1].west = False
grid[6][1].east = False

grid[7][1].north = True
grid[7][1].south = True
grid[7][1].west = False
grid[7][1].east = False

grid[8][1].north = True
grid[8][1].south = True
grid[8][1].west = False
grid[8][1].east = True

grid[9][1].north = True
grid[9][1].south = True
grid[9][1].west = False
grid[9][1].east = False

grid[10][1].north = True
grid[10][1].south = False
grid[10][1].west = False
grid[10][1].east = True

grid[11][1].north = False
grid[11][1].south = False
grid[11][1].west = True
grid[11][1].east = True

grid[12][1].north = False
grid[12][1].south = True
grid[12][1].west = True
grid[12][1].east = False

grid[13][1].north = True
grid[13][1].south = True
grid[13][1].west = True
grid[13][1].east = False

grid[14][1].north = True
grid[14][1].south = False
grid[14][1].west = False
grid[14][1].east = False

grid[15][1].north = False
grid[15][1].south = False
grid[15][1].west = True
grid[15][1].east = True

grid[0][2].north = False
grid[0][2].south = True
grid[0][2].west = True
grid[0][2].east = False

grid[1][2].north = True
grid[1][2].south = True
grid[1][2].west = False
grid[1][2].east = False

grid[2][2].north = True
grid[2][2].south = False
grid[2][2].west = True
grid[2][2].east = False

grid[3][2].north = False
grid[3][2].south = True
grid[3][2].west = False
grid[3][2].east = True

grid[4][2].north = True
grid[4][2].south = False
grid[4][2].west = True
grid[4][2].east = False

grid[5][2].north = False
grid[5][2].south = True
grid[5][2].west = False
grid[5][2].east = True

grid[6][2].north = True
grid[6][2].south = True
grid[6][2].west = False
grid[6][2].east = False

grid[7][2].north = True
grid[7][2].south = True
grid[7][2].west = False
grid[7][2].east = False

grid[8][2].north = True
grid[8][2].south = False
grid[8][2].west = True
grid[8][2].east = False

grid[9][2].north = False
grid[9][2].south = False
grid[9][2].west = False
grid[9][2].east = True

grid[10][2].north = False
grid[10][2].south = False
grid[10][2].west = True
grid[10][2].east = True

grid[11][2].north = False
grid[11][2].south = True
grid[11][2].west = True
grid[11][2].east = False

grid[12][2].north = True
grid[12][2].south = False
grid[12][2].west = False
grid[12][2].east = True

grid[13][2].north = False
grid[13][2].south = False
grid[13][2].west = False
grid[13][2].east = True

grid[14][2].north = False
grid[14][2].south = True
grid[14][2].west = False
grid[14][2].east = True

grid[15][2].north = True
grid[15][2].south = False
grid[15][2].west = True
grid[15][2].east = False

grid[0][3].north = False
grid[0][3].south = False
grid[0][3].west = False
grid[0][3].east = True

grid[1][3].north = False
grid[1][3].south = True
grid[1][3].west = False
grid[1][3].east = True

grid[2][3].north = True
grid[2][3].south = False
grid[2][3].west = False
grid[2][3].east = True

grid[3][3].north = False
grid[3][3].south = False
grid[3][3].west = True
grid[3][3].east = True

grid[4][3].north = False
grid[4][3].south = True
grid[4][3].west = False
grid[4][3].east = True

grid[5][3].north = True
grid[5][3].south = False
grid[5][3].west = True
grid[5][3].east = False

grid[6][3].north = False
grid[6][3].south = True
grid[6][3].west = False
grid[6][3].east = True

grid[7][3].north = True
grid[7][3].south = True
grid[7][3].west = False
grid[7][3].east = False

grid[8][3].north = True
grid[8][3].south = True
grid[8][3].west = False
grid[8][3].east = True

grid[9][3].north = True
grid[9][3].south = False
grid[9][3].west = True
grid[9][3].east = False

grid[10][3].north = False
grid[10][3].south = False
grid[10][3].west = True
grid[10][3].east = True

grid[11][3].north = False
grid[11][3].south = False
grid[11][3].west = False
grid[11][3].east = True

grid[12][3].north = False
grid[12][3].south = True
grid[12][3].west = True
grid[12][3].east = False

grid[13][3].north = True
grid[13][3].south = False
grid[13][3].west = True
grid[13][3].east = False

grid[14][3].north = False
grid[14][3].south = True
grid[14][3].west = True
grid[14][3].east = True

grid[15][3].north = True
grid[15][3].south = False
grid[15][3].west = False
grid[15][3].east = True

grid[0][4].north = False
grid[0][4].south = True
grid[0][4].west = True
grid[0][4].east = True

grid[1][4].north = True
grid[1][4].south = False
grid[1][4].west = True
grid[1][4].east = False

grid[2][4].north = False
grid[2][4].south = True
grid[2][4].west = True
grid[2][4].east = False

grid[3][4].north = True
grid[3][4].south = False
grid[3][4].west = True
grid[3][4].east = False

grid[4][4].north = False
grid[4][4].south = False
grid[4][4].west = True
grid[4][4].east = True

grid[5][4].north = False
grid[5][4].south = True
grid[5][4].west = False
grid[5][4].east = True

grid[6][4].north = True
grid[6][4].south = False
grid[6][4].west = True
grid[6][4].east = False

grid[7][4].north = False
grid[7][4].south = True
grid[7][4].west = False
grid[7][4].east = True

grid[8][4].north = True
grid[8][4].south = False
grid[8][4].west = True
grid[8][4].east = False

grid[9][4].north = False
grid[9][4].south = False
grid[9][4].west = False
grid[9][4].east = True

grid[10][4].north = False
grid[10][4].south = True
grid[10][4].west = True
grid[10][4].east = False

grid[11][4].north = True
grid[11][4].south = True
grid[11][4].west = True
grid[11][4].east = False

grid[12][4].north = True
grid[12][4].south = False
grid[12][4].west = False
grid[12][4].east = True

grid[13][4].north = False
grid[13][4].south = True
grid[13][4].west = False
grid[13][4].east = True

grid[14][4].north = True
grid[14][4].south = False
grid[14][4].west = True
grid[14][4].east = False

grid[15][4].north = False
grid[15][4].south = False
grid[15][4].west = True
grid[15][4].east = True

grid[0][5].north = False
grid[0][5].south = False
grid[0][5].west = True
grid[0][5].east = True

grid[1][5].north = False
grid[1][5].south = True
grid[1][5].west = False
grid[1][5].east = False

grid[2][5].north = True
grid[2][5].south = True
grid[2][5].west = False
grid[2][5].east = False

grid[3][5].north = True
grid[3][5].south = False
grid[3][5].west = False
grid[3][5].east = True

grid[4][5].north = False
grid[4][5].south = False
grid[4][5].west = True
grid[4][5].east = True

grid[5][5].north = False
grid[5][5].south = False
grid[5][5].west = True
grid[5][5].east = False

grid[6][5].north = False
grid[6][5].south = True
grid[6][5].west = False
grid[6][5].east = True

grid[7][5].north = True
grid[7][5].south = False
grid[7][5].west = True
grid[7][5].east = False

grid[8][5].north = False
grid[8][5].south = False
grid[8][5].west = False
grid[8][5].east = True

grid[9][5].north = False
grid[9][5].south = True
grid[9][5].west = True
grid[9][5].east = True

grid[10][5].north = True
grid[10][5].south = False
grid[10][5].west = False
grid[10][5].east = True

grid[11][5].north = False
grid[11][5].south = True
grid[11][5].west = False
grid[11][5].east = True

grid[12][5].north = True
grid[12][5].south = False
grid[12][5].west = True
grid[12][5].east = True

grid[13][5].north = False
grid[13][5].south = False
grid[13][5].west = True
grid[13][5].east = True

grid[14][5].north = False
grid[14][5].south = True
grid[14][5].west = False
grid[14][5].east = True

grid[15][5].north = True
grid[15][5].south = False
grid[15][5].west = True
grid[15][5].east = False

#Top right
#grid[row][column]
grid[6][11].north = True
grid[6][11].south = True
grid[6][11].east = True
grid[6][11].west = False

grid[7][11].north = True
grid[7][11].south = True
grid[7][11].east = True
grid[7][11].west = False

grid[8][11].north = True
grid[8][11].south = False
grid[8][11].east = True
grid[8][11].west = False

grid[6][10].north = True
grid[6][10].south = False
grid[6][10].east = False
grid[6][10].west = True

grid[7][10].north = False
grid[7][10].south = False
grid[7][10].east = False
grid[7][10].west = True

grid[8][10].north = False
grid[8][10].south = True
grid[8][10].east = True
grid[8][10].west = True

grid[6][9].north = False
grid[6][9].south = True
grid[6][9].east = False
grid[6][9].west = False

grid[7][9].north = True
grid[7][9].south = True
grid[7][9].east = True
grid[7][9].west = False

grid[8][9].north = True
grid[8][9].south = False
grid[8][9].east = False
grid[8][9].west = True

grid[6][8].north = True
grid[6][8].south = False
grid[6][8].east = True
grid[6][8].west = False

grid[7][8].north = False
grid[7][8].south = False
grid[7][8].east = True
grid[7][8].west = True

grid[8][8].north = False
grid[8][8].south = False
grid[8][8].east = True
grid[8][8].west = False

grid[6][7].north = False
grid[6][7].south = True
grid[6][7].east = False
grid[6][7].west = True

grid[7][7].north = True
grid[7][7].south = False
grid[7][7].east = False
grid[7][7].west = True

grid[8][7].north = False
grid[8][7].south = True
grid[8][7].east = False
grid[8][7].west = True



newRunner = Runner(0,0,grid)
newRunner2 = Runner2(0,0,grid)

clock = pygame.time.Clock()
while True: #main game loop
    clock.tick(30)
    
    screen.blit(background,(0,0))
    pygame.draw.circle(screen, RUNNER, (53*newRunner.col+25,30*newRunner.row+15), 10, 0)
    pygame.draw.circle(screen, RUNNER2, (53*newRunner2.col+25,30*newRunner2.row+15), 10, 0)
    for event in pygame.event.get():
        
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    newRunner.moveLeft()
                if event.key == K_RIGHT:
                    newRunner.moveRight()
                if event.key == K_DOWN:
                    newRunner.moveDown()
                if event.key == K_UP:
                    newRunner.moveUp()
                if event.key == K_a:
                    newRunner2.moveLeft()
                if event.key == K_d:
                    newRunner2.moveRight()
                if event.key == K_s:
                    newRunner2.moveDown()
                if event.key == K_w:
                    newRunner2.moveUp()
                if event.key == K_SPACE:
                    newRunner.move(0,0)
                    newRunner2.move(0,0)
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()




    pygame.display.update()
