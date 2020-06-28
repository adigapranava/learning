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

run = True
while run:
	#pygame.time.delay(100) #wait for 100 milisecond

	for event in pygame.event.get(): #if key is quit?
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()  #gives the dictionary of all key pressed

	if keys[pygame.K_UP]:
		y -= vel
	if keys[pygame.K_DOWN]:
		y += vel
	if keys[pygame.K_LEFT]:
		x -= vel
	if keys[pygame.K_RIGHT]:
		x += vel

	win.fill((25,0,0))	#filling the rest of the window with color in rgb format
	pygame.draw.rect(win, (0,255,0), (x, y, width, height))	#drawing the rectangle of width,height and position
	pygame.display.update()
pygame.quit()

