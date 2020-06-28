import pygame
pygame.init()	#must for all pygame

pygame.display.set_caption("Pranava")   #window name
win = pygame.display.set_mode((500,500)) #setting  window size

#initial conditions
x = 0
y = 0
vel = 5
height = 30
width = 30
isjump = False
jumpcount = -10

run = True
while run:
	pygame.time.delay(50) #wait for 100 milisecond

	for event in pygame.event.get(): #if key is quit?
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()  #gives the dictionary of all key pressed

	if keys[pygame.K_LEFT] and x >= 0:
			x -= vel
	if keys[pygame.K_RIGHT] and x <= 500 - width:
			x += vel

	if not(isjump):
		if keys[pygame.K_UP] and y >= 0:
			y -= vel
		if keys[pygame.K_DOWN] and y <= 500 - height:
			y += vel
		if keys[pygame.K_SPACE]:
			isjump = True
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


	win.fill((25,0,0))	#filling the rest of the window with color in rgb format
	pygame.draw.rect(win, (0,255,0), (x, y, width, height))	#drawing the rectangle of width,height and position
	pygame.display.update()
pygame.quit()
