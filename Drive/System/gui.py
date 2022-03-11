from re import X
import pygame, sys, time
#from Drive.System import color

with open('Drive/System/data/userinfo.info', 'r') as y:
  global x
  x = y.readlines()
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
    

  def button(self, x, y, szey, szex, color, text):
    mouse_pos = pygame.mouse.get_pos()
    #print(mouse_pos)
    mousex = mouse_pos[0]
    mousey = mouse_pos[1]
    if mousex >= x and mousex <= (x + szex):
      if mousey >= y and mousey <= (y + szey):
    
        print('True')
        color = (255,0,0)
      else:
        print('False')
    else:
      print('False')
    
    
    rect = pygame.draw.rect(self.screen, color, (x, y, szex, szey)) 
    pygame.draw.rect(self.screen, color, rect)
    
    
  def exit(self):
    self.userinfo.close()
    pygame.close()
    exec(open('OS.py').read())
  

  def gui(self):
    self.wiptxt = self.Arial.render('Work in Progress', True, self.BLACK)
    self.user = self.smllArial.render('User: ' + str(self.userinfo), True, self.BLACK)
    
    while self.running:
      self.screen.fill(self.background)
      self.screen.blit(self.wiptxt, self.wiptxt.get_rect(center = self.screen.get_rect().center))
      self.screen.blit(self.user, (10,10))
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              exit()
              
              
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
              exit()
      self.button(10,50,45,90, self.BLACK, 'Hello')        
      
      pygame.display.update()
              
  
    
            
            
    
#print(color.rgb.RED())
window = window()
window.gui()


