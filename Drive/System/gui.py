import pygame, sys, time



class window:
  def __init__(self):
    self.userinfo = open('Drive/System/data/userinfo.info', 'r')
    self.window_name = 'CronOS GUI'
    self.icon = pygame.image.load('Drive/System/data/Logo1.png') 
    self.running = True
    pygame.init()
    pygame.font.init()
    self.screan = pygame.display.set_mode((610,305))
    pygame.display.set_caption(self.window_name)
    pygame.display.set_icon(self.icon)

    
  def exit(self):
    self.userinfo.close()
    pygame.quit()
    return
  

  def gui(self):
    while self.running:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              exit()
              
              
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
              exit()
              
              
  
    
            
            
    

window = window()
window.gui()


