import pygame, sys, time
#from Drive.System import color

FPS = 30
clock=pygame.time.Clock()

with open('Drive/System/data/userinfo.info', 'r') as y:
  global x
  x = y.readlines()





class window:
  def __init__(self):
    self.in_ = False
    self.color = (0,0,0)
    self.FPS = 30
    self.clock=pygame.time.Clock()
    self.resx = 1280
    self.resy = 720
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
    self.MsmllArial = pygame.font.SysFont('Arial',30)
    self.screen = pygame.display.set_mode((self.resx, self.resy))
    pygame.display.set_caption(self.window_name)
    pygame.display.set_icon(self.icon)
    

  def button(self, x, y, szey, szex, Color, text, hover_color, funk):
    self.color = Color
    mouse_pos = pygame.mouse.get_pos()
    
    #print(mouse_pos)
    mousex = mouse_pos[0]
    mousey = mouse_pos[1]
    if mousex >= x and mousex <= (x + szex):
      if mousey >= y and mousey <= (y + szey):
        self.color = hover_color
        
        if pygame.mouse.get_pressed() == (True, False, False):
            self.color = (255,255,255)
            if funk == 'exit':
              exit()
            if funk == 'speed+':
              if self.speed <= 10:
                self.speed +=0.1
            if funk == 'speed-':
              if self.speed >= 0.1:
                self.speed -=0.1
            if funk == 'clear':
              self.screen.fill(self.background)
              
            
      
    
    rect = pygame.draw.rect(self.screen, self.color, (x, y, szex, szey)) 
    pygame.draw.rect(self.screen, self.color, rect)
    words = self.MsmllArial.render(str(text), True, self.BLACK)
    self.screen.blit(words, (x+17, y+7.2))
    
    
  def exit(self):
    try:
      self.userinfo.close()
    except:
      pass
    pygame.quit()
    exec(open('OS.py').read())
  

  def gui(self):
    self.speed = 0.5
    self.hitwall = False
    bounce = []
    bounce.append(0)
    bounce.append(self.resy/2)
    self.wiptxt = self.Arial.render('Work in Progress', True, self.BLACK)
    self.user = self.smllArial.render('User: ' + str(self.userinfo), True, self.BLACK)
    
    while self.running:
      self.screen.blit(self.user, (10,10))
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              exit()
              
              
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
              exit()
              
              
      if bounce[0] >= self.resx-45:
        self.hitwall = True
        self.screen.fill(self.background)
      elif bounce[0] <= 0:
        self.hitwall = False
        self.screen.fill(self.background)
        
      if self.hitwall: 
        bounce[0]-= self.speed
      else:
        bounce[0]+=self.speed
      
      
      self.button(10,50,45,90, (255,0,0), '   +', (200,0,0), 'speed+')     
      self.button(10,100,45,90, (0,255,0), '   - ', (0,200,0), 'speed-') 
      self.button(10,150,45,90, (0,0,255), 'Test', (0,0,200), 'clear')   
      self.button(bounce[0],bounce[1],45,45, (255,0,255), ':)', (255,0,255), False)
      self.button((self.resx-95),5,45,90, (200,0,0), 'Exit', (255,0,0), 'exit')  
      
      self.screen.blit(self.wiptxt, self.wiptxt.get_rect(center = self.screen.get_rect().center))
      
      pygame.display.update()
              
  
    
            
            
    
#print(color.rgb.RED())
window = window()
window.gui()


