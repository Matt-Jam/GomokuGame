import pygame
import sys
class Gomoku:
    def __init__(self):
        #Dimensions of screen
        self.width = 600
        screensize = (self.width,self.width)
        #radius of circle
        self.circle_radius = ((self.width/20)-2)/2
        #Set up pygame window
        pygame.init()
        self.gameDisplay = pygame.display.set_mode(screensize)
        #board grid: 0 is empty, 1 is player 1, -1 is player 2
        self.grid = [[-1 for col in range(20)] for row in range(20)]
        #Colours for different values of grid
        self.colours = {-1:(0,0,255),1:(255,0,0)}
        self.play()
    def GameOver(self):
        return True
    def play(self):
        while not(self.GameOver()):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.gameDisplay.fill(255,255,255)
            self.show()
    def show(self):
        for row in range(20):
            for col in range(20):
                x_pos = (col+0.5)*(self.width/20)
                y_pos = (row+0.5)*(self.width/20)
                pygame.draw.circle(self.gameDisplay,self.colours[self.grid[row][col]],(x_pos,y_pos),self.circle_radius)
game = Gomoku()