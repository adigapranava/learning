import pygame
pygame.init()	#must for all pygame

pygame.display.set_caption("Pranava")   #window name
win = pygame.display.set_mode((500,480)) #setting  window size

WalkRight = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
WalkLeft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

#initial conditions
x = 0
y = 400
vel = 5
height = 64
width = 64
isjump = False
jumpcount = 10
right = False
left = False
walkcount = 0

def redrawGameWindow():
	global walkcount
	win.blit(bg, (0, 0))

	if walkcount + 1 >= 27:
		walkcount = 0

	if left:
		win.blit(WalkLeft[walkcount//3], (x, y))
		walkcount += 1

	elif right:
		win.blit(WalkRight[walkcount//3], (x, y))
		walkcount += 1
	else:
		win.blit(char, (x, y))
	pygame.display.update()

#main loop
run = True
while run:
	pygame.time.delay(50) #wait for 100 milisecond

	for event in pygame.event.get(): #if key is quit?
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()  #gives the dictionary of all key pressed

	if keys[pygame.K_LEFT] and x >= 0:
			x -= vel
			left = True
			right = False
	elif keys[pygame.K_RIGHT] and x <= 500 - width:
			x += vel
			left = False
			right = True
	else:
		left = False
		right = False
		walkcount = 0

	if not(isjump):
		if keys[pygame.K_SPACE]:
			isjump = True
			right = False
			left = False
			walkcount = 0

	else:
		if  jumpcount >= -10:
			neg = 1
			if jumpcount < 0:
				neg = -1
			y -= (jumpcount ** 2) * 0.5 * neg
			jumpcount -= 1
		else:
			isjump = False
			jumpcount = 10
	redrawGameWindow()

pygame.quit()
