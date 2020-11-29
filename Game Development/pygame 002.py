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
gameBoard.fill(white)
x=0
y=0
rectWidth = 100
rectHeight = 100
circleX=200
circleY=200
radius=100
sound = pygame.mixer.Sounde("/Users/BrainMentors/Downloads/gameSound.wav")
while True:
    sound.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #pygame.draw.rect(gameBoard,red,[x,y,rectWidth,rectHeight])

    #pygame.draw.circle(gameBoard,blue,[circleX,circleY],radius)

    
    pygame.display.flip()
