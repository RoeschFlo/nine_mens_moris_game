

import pygame
from pygame.locals import *
import button
from enum import Enum

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
 
class App:
    def __init__(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),
             pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        #defining a font
        smallfont = pygame.font.SysFont('Corbel',35)
        #todo: not used yet
        video_img = pygame.image.load('images/button_video.png').convert_alpha()

        self.text = smallfont.render('quit' , True , (100,100,255))
        
        #game variables
        self.game_state= Enum('PLAY', 'PAUSE')

        #define fonts
        self.font = pygame.font.SysFont("arialblack", 40)
        #define colours 
        self.TEXT_COL= (255,255,255)

    def draw_text(self,text, font, text_color, x, y):
        self.img = font.render(text,True, text_color)
        self._display_surf.blit(self.img,(x,y))
 
    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.game_state = 'PAUSE'
                print("P")
            if event.key == pygame.K_RETURN:
                self.game_state = 'PLAY'
                print("PL")
        if event.type == pygame.QUIT:
            self._running = False
        
    
        
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        self.game_state= 'PAUSE'
        
        #main Game loop
        while( self._running ):
            
            self._display_surf.fill((0,0,0))
            if self.game_state == 'PLAY':
                self.draw_text("Press Space to pause", self.font, self.TEXT_COL, 160,250)
                pygame.display.set_caption("Game-Screen")
            else:
                self.draw_text("Press return to continue", self.font, self.TEXT_COL, 160,250)
                pygame.display.set_caption("Pause-screen")


            for event in pygame.event.get():
                self.event_handler(event)
          
            pygame.display.update()
            # superimposing the text onto our button
            #self._display_surf.blit(self.text , (300,300))
            
        self.on_cleanup()


def main():
    theApp = App()
    theApp.on_execute()

if __name__ == "__main__" :
    main()
    


