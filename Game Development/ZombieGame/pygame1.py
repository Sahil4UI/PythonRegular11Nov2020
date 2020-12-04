
import pygame
import random
from pygame.locals import *
pygame.init()
width=1000
height=600
gameboard = pygame.display.set_mode((width,height))

white=255,255,255
red=255,0,0
blue=0,0,255



target = pygame.image.load('mouseMotion.png')
target=pygame.transform.scale(target,(70,70))

bg = pygame.image.load('bg.png')
bg =pygame.transform.scale(bg,(width,height))

pygame.mouse.set_visible(False)

w = target.get_width()
h = target.get_height()

def timer(seconds):
    font = pygame.font.Font(None,30)
    text = font.render(f"Time Left : {seconds}",True,blue)
    gameboard.blit(text,(400,10))

def main():
    zombieX = random.randint(0,width-150)
    zombieY = random.randint(100,height-300)
    x=0
    y=0
    gunSound = pygame.mixer.Sound("shot_sound.wav")
    zombieList=[]
    seconds =30
    pygame.time.set_timer(USEREVENT,1000)

    
    for i in range(0,5):
        zombie = pygame.image.load(f"zombie{i}.png")
        zombie = pygame.transform.scale(zombie,(150,200))
        zombieList.append(zombie)

    zombieImage = random.choice(zombieList)
    while True:
        gameboard.blit(bg,(0,0))
        for event in pygame.event.get():
            
            #QUIT
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == USEREVENT:
                seconds-=1

            if event.type == pygame.MOUSEBUTTONDOWN:
                gunSound.play()
                if rectTarget.colliderect(rectZombie):
                        zombieX = random.randint(0,width-150)
                        zombieY = random.randint(100,height-300)
                        zombieImage = random.choice(zombieList)
                    
        
        gameboard.blit(zombieImage,(zombieX,zombieY))
        
                

        x=pygame.mouse.get_pos()[0]
        y=pygame.mouse.get_pos()[1]
        # gameboard.blit(zombie1,(zombieX,zombieY))
               
        rectZombie = pygame.Rect(zombieX,zombieY,150,200)
        rectTarget = pygame.Rect(x,y,70,70)
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


     
        timer(seconds)
        
        #flip updates only the region where changes has been made
        pygame.display.flip()
main()
