import pygame, time

class window:
  def __init__(self):
    self.def_window_name = 'Unnamed Window'
    self.def_icon = pygame.image.load('Logo.png')  

  def init():
    pygame.init()
    pygame.font.init()

  def create_win(self, x_y, name):
    returns = pygame.display.set_mode((x_y))
    
    if name == '':
      pygame.display.set_caption(self.def_window_name)
    else:
      pygame.display.set_caption(name)

    return returns

    
  

window = window



