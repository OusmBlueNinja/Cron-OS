szex = 5
szey = 5

x = 4
y = 4


#pygame.draw.rect(screan, color, (x, y, szex, szey)) 
while True:
  mousex = int(input('x >> '))
  mousey = int(input('y >> '))
  if (mousex >= x) and (mousex <= szex):
    if (mousey >= y) and (mousey <= szey):
      print('True')

  else:
    print('False')
  