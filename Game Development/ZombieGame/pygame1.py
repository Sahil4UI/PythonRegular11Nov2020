
import pygame
pygame.init()
width=1000
height=600
gameboard = pygame.display.set_mode((width,height))

white=255,255,255
red=255,0,0
blue=0,0,255

x=0
y=0

target = pygame.image.load('mouseMotion.png')
target=pygame.transform.scale(target,(70,70))

bg = pygame.image.load('bg.jpg')
bg =pygame.transform.scale(bg,(width,height))

pygame.mouse.set_visible(False)

w = target.get_width()
h = target.get_height()
while True:
    gameboard.blit(bg,(0,0))
    for event in pygame.event.get():
        #QUIT
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.MOUSEMOTION:
            x=event.pos[0]
            y=event.pos[1]


           
    #pygame.draw.rect(gameboard,red,[x,y,w,h])
    gameboard.blit(target,[x-(w/2),y-(h/2)])
    
  
    if x>width-w:
        movex=-1
    elif x<0:
        movex=1
    if y>height-h:
        movey=-1
    elif y<0:
        movey=1
    #pygame.draw.circle(gameboard,blue,[cx,cy],r)


 

    #flip updates only the region where changes has been made
    pygame.display.flip()
