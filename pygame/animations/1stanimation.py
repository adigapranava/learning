import pygame
pygame.init()	#must for all pygame

pygame.display.set_caption("Pranava")   #window name
win = pygame.display.set_mode((500,480)) #setting  window size

WalkRight = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')] #mans right side motion
WalkLeft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')] #mans left side motion
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

#initial conditions
clock = pygame.time.Clock() #games clock

bulletSound = pygame.mixer.Sound('bullet.wav') 
hitSound = pygame.mixer.Sound('hit.wav')

music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1) # -1 for looping

score = 0

class player(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 5
		self.isjump = False
		self.jumpcount = 10
		self.right = False
		self.left = False
		self.walkcount = 0
		self.standing = True
		self.hitbox = (self.x + 18, self.y + 15, 25, 50) #for collision check

	def draw(self):
		if self.walkcount + 1 >= 27:
			self.walkcount = 0

		if not(self.standing):
			if self.left:
				win.blit(WalkLeft[self.walkcount//3], (self.x, self.y)) #for 3 run of main loop same image will be displayed
				self.walkcount += 1

			elif self.right:
				win.blit(WalkRight[self.walkcount//3], (self.x, self.y))
				self.walkcount += 1
		else:
			if self.right:
				win.blit(WalkRight[0], (self.x, self.y))
			else:
				win.blit(WalkLeft[0], (self.x, self.y))
		self.hitbox = (self.x + 18, self.y + 15, 25, 50)
		#pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

	def hit(self):
		self.isjump = False
		self.jumpcount = 10
		self.x = 60
		self.y = 400
		walkcount = 0
		font1 = pygame.font.SysFont('comicsans', 100)
		text = font1.render('-5', 1, (250,0,0))
		win.blit(text, (250 - text.get_width() / 2, 250))
		pygame.display.update()
		i = 0
		while i < 100: 	#to wait for 2-3 sec
			pygame.time.delay(10)
			i += 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					i = 301
					pygame.quit()


class  projectile(object):
	def __init__(self, x, y, radius, color, facing):
		self.x = x
		self.y = y
		self.radius = radius
		self.vel = 7
		self.color = color
		self.facing = facing

	def draw(self,win):
		pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


		
class enemy():
	WalkRight = [ pygame.image.load('R1E.png'),pygame.image.load('R2E.png'),pygame.image.load('R3E.png'),pygame.image.load('R4E.png'),pygame.image.load('R5E.png'),pygame.image.load('R6E.png'),pygame.image.load('R7E.png'),pygame.image.load('R8E.png'),pygame.image.load('R9E.png'),pygame.image.load('R10E.png'),pygame.image.load('R11E.png')]
	WalkLeft = [ pygame.image.load('L1E.png'),pygame.image.load('L2E.png'),pygame.image.load('L3E.png'),pygame.image.load('L4E.png'),pygame.image.load('L5E.png'),pygame.image.load('L6E.png'),pygame.image.load('L7E.png'),pygame.image.load('L8E.png'),pygame.image.load('L9E.png'),pygame.image.load('L10E.png'),pygame.image.load('L11E.png')]
	def __init__(self, x, y, width, height, end):	
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.end = end
		if self.x < self.end:
			self.path = [self.x, self.end]
		else:
			self.path = [self.end, self.x]
		self.vel = 3
		self.walkcount = 0
		self.life = 10
		self.visible = True
		self.hitbox = (self.x + 17, self.y + 2, 31, 57)

	def draw(self,win):	 #all drawing material
		self.move()
		if self.visible:
			if self.walkcount + 1 >= 33:
				self.walkcount = 0
			if self.vel > 0:
				win.blit(self.WalkRight[self.walkcount // 3], (self.x, self.y))
				self.walkcount += 1
			else:
				win.blit(self.WalkLeft[self.walkcount // 3], (self.x, self.y))
				self.walkcount += 1
			pygame.draw.rect(win, (255, 0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
			pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.life))    , 10))
			self.hitbox = (self.x + 17, self.y + 2, 31, 57)
			#pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

	def move(self):	#all stearing and control stuff
		if self.vel > 0:
			if self.x + self.vel < self.path[1]:
				self.x += self.vel
			else:
				self.vel = -self.vel
				self.walkcount = 0
		else:
			if self.x - self.vel > self.path[0]:
				self.x += self.vel
			else:
				self.vel = -self.vel
				self.walkcount = 0
	def hit(self):
		if self.life > 1:
			self.life -= 1
		else:
			self.visible = False
		print("hit")

font = pygame.font.SysFont('comicsans', 30, True)
man = player(0, 400, 64, 64)
enemy1 = enemy(100, 400, 64, 64, 460)
bullets = []
shootloop = 0

def redrawGameWindow():	#redrawing all stufs
	global walkcount
	win.blit(bg, (0, 0))
	text = font.render('Score : ' + str(score), 1, (10, 10, 10))
	win.blit(text, (380, 10))
	enemy1.draw(win)
	man.draw()
	for bullet in bullets: #all bullets
		bullet.draw(win)
	pygame.display.update()

run = True
while run:
	clock.tick(27) #wait for 100 milisecond

	if enemy1.visible:
		if man.hitbox[1] + man.hitbox[3] > enemy1.hitbox[1] and man.hitbox[1] < enemy1.hitbox[1] + enemy1.hitbox[3]:
			if man.hitbox[0] + man.hitbox[2] > enemy1.hitbox[0] and man.hitbox[0] < enemy1.hitbox[0] + enemy1.hitbox[2]:
				man.hit()
				score -= 5

	if shootloop > 0:
		shootloop += 1
	if shootloop > 3:
		shootloop = 0

	for event in pygame.event.get(): #if key is quit?
		if event.type == pygame.QUIT:
			run = False
	for bullet in bullets:
		if bullet.x < 500 and bullet.x > 0:
			bullet.x += bullet.vel * bullet.facing
		else:
			bullets.pop(bullets.index(bullet))#removing the bullet
		if enemy1.visible:
			if bullet.y + bullet.radius > enemy1.hitbox[1] and bullet.y - bullet.radius < enemy1.hitbox[1] + enemy1.hitbox[3]:
				if bullet.x + bullet.radius > enemy1.hitbox[0] and bullet.x - bullet.radius < enemy1.hitbox[0] + enemy1.hitbox[2]:
					hitSound.play()
					enemy1.hit()  
					score += 1
					bullets.pop(bullets.index(bullet))

	keys = pygame.key.get_pressed()  #gives the dictionary of all key pressed

	if keys[pygame.K_SPACE] and shootloop == 0:
		bulletSound.play()
		facing = 1
		if man.left:
			facing = -1
		if len(bullets) < 5:
			bullets.append(projectile(round(man.x + man.width // 2),round(man.y + man.height // 2), 6, (0,0,0), facing))
			shootloop = 1

	if keys[pygame.K_LEFT] and man.x >= 0:
			man.x -= man.vel
			man.left = True
			man.right = False
			man.standing = False
	elif keys[pygame.K_RIGHT] and man.x <= 500 - man.width:
			man.x += man.vel
			man.left = False
			man.right = True
			man.standing = False
	else:
		man.standing = True
		man.walkcount = 0

	if not(man.isjump):
		if keys[pygame.K_UP]:
			man.isjump = True
			man.standing = False
			man.walkcount = 0

	else:
		if  man.jumpcount >= -10:
			neg = 1
			if man.jumpcount < 0:
				neg = -1
			man.y -= (man.jumpcount ** 2) * 0.5 * neg
			man.jumpcount -= 1
		else:
			man.isjump = False
			man.jumpcount = 10
	redrawGameWindow()

pygame.quit()
