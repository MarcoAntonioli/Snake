import pygame
import random

head_color = (0,90,0)											#marking colors I will need
background = (180,200,100)
white = (255,255,255)
tail_color = (30,150,30)    
food_color = (200,50,30)
width = height = n = 600
dimension = n//30

def grid(screen,n):												#function to draw grid in the screen
	screen.fill(background)										#fill the screen with a choice color
	for i in range(dimension,n,dimension):
		pygame.draw.line(screen,white,(i,0),(i,n),1)
		pygame.draw.line(screen,white,(0,i),(n,i),1)


def snake(snakel,surface,length,x,y,done):						#define the snake
	for snake in snakel:
		head = snakel[len(snakel)-1]
		if snake == head:
			color = head_color
		else:
			color = tail_color
		pygame.draw.rect(surface,color,[snake[0],snake[1],dimension+1,dimension+1])
	cube = [x,y]
	snakel.append(cube)

	if len(snakel) > length:
		del snakel[0]
		head = snakel[len(snakel)-1]

def move(event,x_update,y_update):								#function to move the snake
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			x_update = -dimension
			y_update = 0
		elif event.key == pygame.K_RIGHT:
			x_update = dimension
			y_update = 0
		elif event.key == pygame.K_UP:
			x_update = 0
			y_update = -dimension
		elif event.key == pygame.K_DOWN:
			x_update = 0
			y_update = dimension
	return x_update, y_update									

def apple_gen():
	food_x = (random.randint(0,(width - dimension)//dimension))*dimension
	food_y = (random.randint(0,(height - dimension)//dimension))*dimension
	return food_x, food_y

def food(surface,food_x,food_y):					#function to create food
	pygame.draw.rect(surface,food_color,[food_x,food_y,dimension+1,dimension+1])
	#return food_x, food_y


def checks(snakel,x,y,done):
	if not -(dimension//2) < x < n:
		done = True
	if not -(dimension//2) < y < n:
		done = True
	# for i in range(len(snakel)-1):
	# 	for j in range(i+1, len(snakel)-1):
	# 		if snakel[i][0] == snakel[j][0] and snakel[i][1] == snakel[j][1]:
	# 			done = True
	for snake in snakel[:len(snakel)-1]:
		if snake == snakel[len(snakel)-1]:
			done = True
	return done


def gameover(screen,game_over,done):				#game over funciton
	screen.fill(white)
	lost = pygame.font.SysFont(None, 50).render('Game Over!', True, food_color)
	option1 = pygame.font.SysFont(None, 50).render('Press Q to quit', True, food_color)
	option2 = pygame.font.SysFont(None, 50).render('Press R to restart', True, food_color)
	screen.blit(lost,[width//4,height//4])
	screen.blit(option1,[width//4,height//4+50])
	screen.blit(option2,[width//4,height//4+100])
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				start()
			if event.key == pygame.K_q:
				game_over = True
				done = False
		elif event.type == pygame.QUIT:
			game_over = True
			done = False
	return game_over, done

def start(): 													#main function 
#Initializing some variables

	pygame.init() 												#initializes pygame
	#pygame.display.init()										#initializes pygame.display
	pygame.display.set_caption("Snake v1.0")					#Title of the window
	screen = pygame.display.set_mode((width,height)) 			#Creates screen
	clock = pygame.time.Clock()									#creates the clock
	x = (width // (dimension * 4)) * dimension					#starts decentred
	y = (height // (dimension * 4)) * dimension  
	x_update = 0												#update moves set to 0 
	y_update = 0
	snake_speed = 10											#arbitrarily chosen snake speed 
	food_x, food_y = apple_gen()
	snakel = [[x,y]]											#initializes the snake with just the head position
	length = 1													#starting maximum length is 1 (of course)
	score = 0
#Core part


	game_over = False											#set game_over to False for the while loop	
	done = False												#same dor done
	while not game_over: 										#while game_over is False
		for event in pygame.event.get():						#for every event
			if event.type == pygame.QUIT: 						#if it is the x tab in the windown
				game_over = True								#stops the cycle if game_over is True
			x_update, y_update = move(event,x_update,y_update)	#movement in variable x and y
		while done:												#if it happens that done is True, than game over screen
			game_over, done = gameover(screen,game_over,done)
		x += x_update											#update x and y varuables with the movement
		y += y_update
		grid(screen,n)											#creates the grid on the screen
		score_ = pygame.font.SysFont(None, 40).render(f"Score: {score}", True, food_color)
		screen.blit(score_,[dimension,dimension])
		done = checks(snakel,x,y,done)							#performs boundaries checks and suicide check			


		food(screen,food_x,food_y)                 				#displays food
		snake(snakel,screen,length,x,y,done)					#creates the snake
		if x == food_x and y == food_y:							#if it catches the apple
			print('Gnam!')										#then print Gnam! and
			food_x, food_y = apple_gen()						#change food position
			length += 1											#increment maximum length by 1
			score += 1											#increment score

#After all the operations it refreshes the screen
		pygame.display.update()									#updates the window
		clock.tick(snake_speed)

#De-initializing and closing
	#pygame.display.quit()
	pygame.quit()												#being gentle with the IDLE, semicit.
	quit()

#call the main frame and start the game
start()






