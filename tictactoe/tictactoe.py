# TIC-TAC-TOE (cross-zero game)
# Code written by: Tapan Bohra
# Institute : IITK


import pygame,sys, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

FPS = 15
windowwidth=300
windowheight=300
cellsize=100
assert windowwidth%cellsize==0, "Windowsize has to be divisible by Cellsize"
assert windowheight%cellsize==0, "Windowheight  has to be divisible by Cellsize"
cellwidth= windowwidth/cellsize
cellheight= windowheight/cellsize

WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
DARKBLUE  = ( 0 ,   0, 155)
ORANGE    = (250, 175,   0)
BGCOLOR = BLACK
NAVYBLUE =  ( 60,  60,  60)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
DARKTURQUOISE = (  3,  54,  73)

b1 = pygame.Rect(0, 0, cellsize, cellsize)
b2 = pygame.Rect(100, 0, cellsize, cellsize)
b3 = pygame.Rect(200, 0, cellsize, cellsize)
b4 = pygame.Rect(0, 100, cellsize, cellsize)
b5 = pygame.Rect(100, 100, cellsize, cellsize)
b6 = pygame.Rect(200, 100, cellsize, cellsize)
b7 = pygame.Rect(0, 200, cellsize, cellsize)
b8 = pygame.Rect(100, 200, cellsize, cellsize)
b9 = pygame.Rect(200, 200, cellsize, cellsize)

def main():
	global DISPSURF,FONTOBJ,FPSCLOCK
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPSURF = pygame.display.set_mode((windowwidth,windowheight))
	FONTOBJ = pygame.font.Font('freesansbold.ttf', 18)
	pygame.display.set_caption('TIC TAC TOE')
	showstartscreen()
	while 1:
		who_won=rungame()        # who_won tells us which player has won
		showgameoverscreen(who_won)



def showstartscreen():
	DISPSURF.fill(DARKTURQUOISE)
	startfont=pygame.font.Font('freesansbold.ttf', 35)
	startsurf=startfont.render('TIC-TAC-TOE',True,WHITE,DARKGREEN)
	startrect=startsurf.get_rect()
	startrect.center=(windowwidth/2,30)
	DISPSURF.blit(startsurf,startrect)
	player1= ask(DISPSURF, "Player1")
	f=open('player_names.txt','w')
	f.write("%s "%player1)
	player2= ask(DISPSURF, "Player2")
	f.write("%s"%player2)
	f.close()
		

	while 1:
#		drawpresskeymsg()

        	if checkforkeypress():
           		pygame.event.get() # clear event queue
         	   	return

		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
		
		pygame.display.update()
		FPSCLOCK.tick(FPS)


def ask(DISPSURF, question):
	"ask(DISPSURF, question) -> answer"
  	pygame.font.init()
  	current_string = []
  	display_box(DISPSURF, question + ": " + string.join(current_string,""))
  	
	while 1:
    		inkey = get_key()
    		if inkey == K_BACKSPACE:
      			current_string = current_string[0:-1]
    		elif inkey == K_RETURN:
      			break
    		elif inkey == K_MINUS:
      			current_string.append("_")
    		elif inkey <= 127:
     			 current_string.append(chr(inkey))
    	
		display_box(DISPSURF, question + ": " + string.join(current_string,""))
  	
	return string.join(current_string,"")


def get_key():
	
	while 1:
    		event = pygame.event.poll()
    		if event.type == KEYDOWN:
      			return event.key
    		else:
      			pass


def display_box(DISPSURF, message):
	
	"Print a message in a box in the middle of the screen"
  	fontobject = pygame.font.Font(None,18)
  	pygame.draw.rect(DISPSURF, (255,255,255),((DISPSURF.get_width() / 2) - 100, (DISPSURF.get_height() / 2) - 10, 200,25), 0)
  	pygame.draw.rect(DISPSURF, (0,0,0), ((DISPSURF.get_width() / 2) - 102, (DISPSURF.get_height() / 2) - 12, 204,27), 1)
  
	if len(message) != 0:
    		DISPSURF.blit(fontobject.render(message, 1, DARKBLUE), ((DISPSURF.get_width() / 2) - 100, (DISPSURF.get_height() / 2) - 10))
	pygame.display.flip()


def drawpresskeymsg():
	keypress=FONTOBJ.render('Press a key to play',True, DARKBLUE,DARKGREEN)
	keypressrect= keypress.get_rect()
	keypressrect.topleft = (windowwidth - 200, windowheight - 30)
	DISPSURF.blit(keypress,keypressrect)
	

def checkforkeypress():
	if len(pygame.event.get(QUIT)) > 0:
        	pygame.quit()
		sys.exit()

    	keyUpEvents = pygame.event.get(KEYUP)
   	
	if len(keyUpEvents) == 0:
        	return None
    	
	if keyUpEvents[0].key == K_ESCAPE:
        	pygame.quit()
		sys.exit()
    	
	return keyUpEvents[0].key

def rungame():
	DISPSURF.fill(WHITE)
      	drawgrid()
	pygame.display.update()
	a=[]
	b=[]
	for i in range(0,9):
		a.append(0)
		b.append(0)
	flag=0
	while 1:
		for event in pygame.event.get(): # event handling loop
			if event.type == QUIT:
				pygame.quit()
				sys.exit()			
			
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
			        	pygame.quit()
					sys.exit()
				

			elif event.type == MOUSEBUTTONUP:
				flag+=1
                		mousex, mousey = event.pos
                		clickedbutton = getButtonClicked(mousex, mousey)
				row=(clickedbutton-1)/3+1
                		column=clickedbutton%3
				if(column==0):
					column=3
		
				if(flag%2!=0):
					centerx= 50*(2*column-1)
					centery= 50*(2*row-1)
					pygame.draw.circle(DISPSURF,BLACK,(centerx,centery),40,0)
					a[clickedbutton-1]=1
					if(a[0]==1 and a[1]==1 and a[2]==1):
						return 1
					elif(a[3]==1 and a[4]==1 and a[5]==1):
						return 1
					elif(a[6]==1 and a[7]==1 and a[8]==1):
						return 1
					elif(a[0]==1 and a[3]==1 and a[6]==1):
						return 1
					elif(a[2]==1 and a[5]==1 and a[8]==1):
                                                return 1
					elif(a[1]==1 and a[4]==1 and a[7]==1):
                                                return 1
					elif(a[0]==1 and a[4]==1 and a[8]==1):
                                                return 1
					elif(a[2]==1 and a[4]==1 and a[6]==1):
                                                return 1

				elif(flag%2==0):
					centerx= 50*(2*column-1) 		
					centery= 50*(2*row-1)
					pygame.draw.line(DISPSURF,BLACK,(centerx-30,centery-30),(centerx+30,centery+30),10)
					pygame.draw.line(DISPSURF,BLACK,(centerx-30,centery+30),(centerx+30,centery-30),10)
					b[clickedbutton-1]=1
					if(b[0]==1 and b[1]==1 and b[2]==1):
                                                return 2
                                        elif(b[3]==1 and b[4]==1 and b[5]==1):
                                                return 2
                                        elif(b[6]==1 and b[7]==1 and b[8]==1):
                                                return 2
                                        elif(b[0]==1 and b[3]==1 and b[6]==1):
                                                return 2
                                        elif(b[2]==1 and b[5]==1 and b[8]==1):
                                                return 2
                                        elif(b[1]==1 and b[4]==1 and b[7]==1):
                                                return 2
                                        elif(b[0]==1 and b[4]==1 and b[8]==1):
                                                return 2
                                        elif(b[2]==1 and b[4]==1 and b[6]==1):
                                                return 2

				if(flag==9):
					return 0
				
				pygame.display.update()
       				FPSCLOCK.tick(FPS)


def getButtonClicked(x, y):
	if b1.collidepoint( (x, y) ):
        	return 1 
    	elif b2.collidepoint( (x, y) ):
        	return 2
    	elif b3.collidepoint( (x, y) ):
        	return 3
    	elif b4.collidepoint( (x, y) ):
        	return 4
    	elif b5.collidepoint( (x, y) ):
                return 5
	elif b6.collidepoint( (x, y) ):
              	 return 6
	elif b7.collidepoint( (x, y) ):
                return 7
	elif b8.collidepoint( (x, y) ):
                return 8
	elif b9.collidepoint( (x, y) ):
                return 9
	
	return None
	


	
def drawgrid():
	for x in range(0, windowwidth, cellsize): # draw vertical lines
        	pygame.draw.line(DISPSURF, DARKGRAY, (x, 0), (x, windowheight),2)
	for y in range(0, windowheight, cellsize): # draw horizontal lines
        	pygame.draw.line(DISPSURF, DARKGRAY, (0, y), (windowwidth, y),2)

			
def showgameoverscreen(who_won):
	DISPSURF.fill(DARKTURQUOISE)
	gameoverobj=pygame.font.Font('freesansbold.ttf', 35)
	f=open('player_names.txt','r')
	x=f.readline()
	player1,player2=x.split(' ')
	if(who_won==0):
		who=gameoverobj.render('Nobody Won',True,DARKGREEN)
		whorect=who.get_rect()
		whorect.center=(windowwidth/2,60)
		DISPSURF.blit(who,whorect)
	
	if(who_won==1):
		who=gameoverobj.render('%s Wins'%player1,True,WHITE)
                whorect=who.get_rect()
                whorect.center=(windowwidth/2,60)
                DISPSURF.blit(who,whorect)

	if(who_won==2):
	 	who=gameoverobj.render('%s Wins'%player2,True,WHITE)
                whorect=who.get_rect()
                whorect.center=(windowwidth/2,60)
                DISPSURF.blit(who,whorect)

		
	gameover=gameoverobj.render('GAME OVER',True,WHITE)
	gameoverrect=gameover.get_rect()
	gameoverrect.center= (windowwidth/2,windowheight/2)
	DISPSURF.blit(gameover,gameoverrect)
	drawpresskeymsg()

 	while True:
		pygame.display.update()
 	 	if checkforkeypress():
            		pygame.event.get() # clear event queue
            		return

	
	
if __name__=='__main__':
	main()
