import pygame, sys, time
from Drive.System import color

with open('Drive/System/data/userinfo.info', 'r') as y:
  global x
  x = y.readlines(0)
class window:
  def __init__(self):
    
    self.resx = 720
    self.resy = 405
    self.userinfo = x
    print(self.userinfo)
    self.window_title = 'CronOS GUI v1.0.0'
    self.window_name = self.window_title
    self.icon = pygame.image.load('Drive/System/data/Logo1.png') 
    self.running = True
    self.background = (127, 127, 127)
    self.BLACK = (0,0,0)
    pygame.init()
    pygame.font.init()
    self.Arial = pygame.font.SysFont('Arial',35)
    self.smllArial = pygame.font.SysFont('Arial',20)
    self.screen = pygame.display.set_mode((self.resx, self.resy))
    pygame.display.set_caption(self.window_name)
    pygame.display.set_icon(self.icon)
    

  def button(self, posx, posy, size_x, size_y, color, text):
    rect = (pos, (posx + size_x), (posy - size_y), (pos ))
    pygame.draw.rect(self.screen, color, rect)
    
  def exit(self):
    self.userinfo.close()
    pygame.close()
    exec(open('OS.py').read())
  

  def gui(self):
    self.screen.fill(self.background)
    self.wiptxt = self.Arial.render('Work in Progress', True, self.BLACK)
    self.user = self.smllArial.render('User: ' + str(self.userinfo), True, self.BLACK)
    while self.running:
      self.screen.blit(self.wiptxt, self.wiptxt.get_rect(center = self.screen.get_rect().center))
      self.screen.blit(self.user, (10,10))
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              exit()
              
              
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
              exit()
              
      
      pygame.display.update()
              
  
    
            
            
    
#print(color.rgb.RED())
window = window()
window.gui()


