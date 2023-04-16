#code from https://github.com/russs123/pygame_tutorials/blob/main/Menu/button.py
import pygame

#button class
class Button():
	def __init__(self, x, y, text, size, lenght):
		
		
		self.x = x
		self.y = y
		self.clicked = False
		self.text = text
		self.size = size
		self.length = lenght

	def draw(self, surface):
		
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()
		pygame.draw.rect()
		'''
		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action'''
		pass