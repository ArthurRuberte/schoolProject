#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

pygame.init
fenetre = pygame.display.set_mode((2160, 720), RESIZABLE)

fond = pygame.image.load("maxresdefault.jpg").convert()
fenetre.blit(fond, (0,0))

garde1 = pygame.image.load("garde1.png").convert_alpha()
position_garde1 = garde1.get_rect()

stone = pygame.image.load("stone.jpg").convert()
position_stone = stone.get_rect()

feuille = pygame.image.load("feuille.png").convert()
position_feuille = feuille.get_rect()

water = pygame.image.load("water.jpg").convert()
position_water = water.get_rect()
#~ water = pygame.transform.scale(water, (150,150))

wood = pygame.image.load("wood.jpg").convert()
position_wood = wood.get_rect()

village1 = pygame.image.load("village1.png").convert()
position_village1 = village1.get_rect()

fond_village1 = pygame.image.load("fond.jpg").convert()

perso = pygame.image.load("sprite_face_depart.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, (100,100))
perso_x = 0
perso_y = 0

x = position_perso[0]
y = position_perso[1]

switch = 0
switch1 = 0
switch2 = 0
switch3 = 0

pygame.display.flip()

pygame.key.set_repeat(400,30)

def collision(x, y, a, b, taille):
	return x>=a and x<=a+taille and y>=b and y<=b+taille


 
class Block(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, image, x=800,y=100):
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)
		# Instead we could load a proper pciture of a car...
		self.image = pygame.image.load(image).convert_alpha()
		# Fetch the rectangle object that has the dimensions of the image.
		self.rect = pygame.Rect(x,y,self.image.get_rect()[2], self.image.get_rect()[3])
		self.mask = pygame.mask.from_surface(self.image)
		

sblock = Block("stone.jpg", 800, 100)
sblock2 = Block("feuille.png", 1000, 100)
sblock3 = Block("water.jpg", 400,100)
sblock4 = Block("water.jpg", 400,-150)
sblock5 = Block("water.jpg", 400,500)
sblock6 = Block("garde1.png", 650, 500)
sblock7 = Block("village1.png", 200, 200)

class Perso(pygame.sprite.Sprite):
    
    def __init__(self, image, x=0,y=0):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image).convert_alpha()
		
		self.rect = pygame.Rect(x,y,self.image.get_rect()[2], self.image.get_rect()[3])
		self.mask = pygame.mask.from_surface(self.image)
	
    def move(self, x, y):
		self.rect = self.rect.move(x,y)
	
sperso = Perso("sprite_face_depart.png", 0, 0)

DEBUG=True

#~ position_perso.x>=position_stone.x and position_perso.x<=position_stone.x + 80 and position_perso.y>=position_stone.y and position_perso.y<=position_stone.y + 80

continuer = 1
while continuer:
		
	prevposition = sperso.rect
	
	for event in pygame.event.get():
			if event.type == QUIT:
				continuer = 0
			if event.type == KEYDOWN:

							
				if event.key == K_s:	
					sperso.move(0,10)
					print("down", sperso.rect)
	
				if event.key == K_z:
					sperso.move(0,-10)
					print("up",sperso.rect)
					
				if event.key == K_q:
					sperso.move(-10,0)
					print("left",sperso.rect)
					
				if event.key == K_d:
					sperso.move(10,0)
					print("right",sperso.rect)
		
			
			obstacles = [sblock, sblock2, sblock3, sblock4, sblock5, sblock6, sblock7]
			for obst in obstacles:
				if pygame.sprite.collide_mask(sperso, obst) != None :
					print('collision masque')
					print(prevposition)
					print(sperso.rect)
					sperso.rect = prevposition
			if pygame.sprite.collide_mask(sperso, sblock) != None :	
				print('collision masque')
				print(prevposition)
				print(sperso.rect)
				sperso.rect = prevposition
		 	elif pygame.sprite.collide_mask(sperso, sblock2) != None :
				print('collision masque')
				print(prevposition)
				print(sperso.rect)
				sperso.rect = prevposition
			elif pygame.sprite.collide_mask(sperso, sblock3) != None :
				print('collision masque')
				print(prevposition)
				print(sperso.rect)
				sperso.rect = prevposition
			elif pygame.sprite.collide_mask(sperso, sblock4) != None :
				print('collision masque')
				print(prevposition)
				print(sperso.rect)
				sperso.rect = prevposition
			elif pygame.sprite.collide_mask(sperso, sblock5) != None :
				print('collision masque')
				print(prevposition)
				print(sperso.rect)
				sperso.rect = prevposition
			elif pygame.sprite.collide_mask(sperso, sblock6) != None :
				print('collision masque')
				print(prevposition)
				print(sperso.rect)
				print("salut mon ami! Bienvenue!")
				sperso.rect = prevposition
			elif pygame.sprite.collide_mask(sperso, sblock7) != None :
				print('collision masque')
				print(prevposition)
				print(sperso.rect)
				sperso.rect = prevposition
				fenetre.blit(fond_village1, (0,0))
				
			fenetre.blit(fond, (0,0))
			fenetre.blit(fond, (1080, 0))	
			fenetre.blit(sblock.image, sblock.rect)
			#fenetre.blit(sblock.image, (100,500))
			fenetre.blit(sblock2.image, sblock2.rect)
			fenetre.blit(sblock3.image, sblock3.rect)
			fenetre.blit(sblock4.image, sblock4.rect)
			fenetre.blit(water, (400,350))
			fenetre.blit(sblock5.image, sblock5.rect)
			fenetre.blit(wood, (400,400))
			fenetre.blit(wood, (475,400))
			fenetre.blit(wood, (550,400))
			fenetre.blit(wood, (570,400))
			fenetre.blit(wood, (400,350))
			fenetre.blit(wood, (475,350))
			fenetre.blit(wood, (550,350))
			fenetre.blit(wood, (570,350))
			fenetre.blit(sblock7.image, sblock7.rect)
			fenetre.blit(sperso.image, sperso.rect)
			fenetre.blit(sblock6.image, sblock6.rect)
			
			
			pygame.display.flip()
			pygame.display.update()
			

#~ def spawn_blocks(block, x, y, direction, nombre):
	#~ coord = []
	#~ if direction == "hd":
		#~ for n in range(nombre):
			#~ x,y = pos
			#~ coord.append((x,y))





