import pygame, time

class gui:
  def __init__(self):
    pygame.init()
    pygame.font.init()
    self.window_size = (400, 711)
    self.window_name = 'CronOS GUI'
    self.icon = pygame.image.load('Logo.png') 
    self.Arial = pygame.font.SysFont('Arial',35)

  def makeWin(self):
    

    self.screan = pygame.display.set_mode(self.window_size)
    pygame.display.set_caption(self.window_name)
    pygame.display.set_icon(self.icon)

  def drawTime():
    #pygame.draw.rect(screan, COLLOR2, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    return
    


  def exit(self):
    pygame.display.quit()

gui = gui()
gui.makeWin()
time.sleep(5)
gui.exit()