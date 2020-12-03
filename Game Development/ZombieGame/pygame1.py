
import pygame
import random
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

zombie1 = pygame.image.load('zombie.png')
zombie1 = pygame.transform.scale(zombie1,(150,200))


def main():
    zombieX = random.randint(0,width-150)
    zombieY = random.randint(100,height-300)
    x=0
    y=0
    gunSound = pygame.mixer.Sound("shot_sound.wav")
    
    while True:
        gameboard.blit(bg,(0,0))
        for event in pygame.event.get():
            
            #QUIT
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                gunSound.play()
                if rectTarget.colliderect(rectZombie):
                        zombieX = random.randint(0,width-150)
                        zombieY = random.randint(100,height-300)
                    
                
                
        
                

        x=pygame.mouse.get_pos()[0]
        y=pygame.mouse.get_pos()[1]
        gameboard.blit(zombie1,(zombieX,zombieY))
               
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


     

        #flip updates only the region where changes has been made
        pygame.display.flip()
main()
