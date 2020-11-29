import pygame
pygame.init()
width=1000
height=600
gameBoard = pygame.display.set_mode((width,height))
black = 0,0,0
red = 255,0,0
blue = 0,0,255
green = 0,255,0
white = 255,255,255

x=0
y=0
rectWidth = 50
rectHeight = 50
circleX=200
circleY=200
radius=100

while True:
    gameBoard.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.draw.rect(gameBoard,red,[x,y,rectWidth,rectHeight])
    x+=5


    
    pygame.display.flip()
