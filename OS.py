import time, json, os, sys, os.path, filecmp
from Drive.System.packages import pkgM
from Drive.System import color
from Drive.System import load

with open('Drive/System/users.json', 'r') as x:
    y = json.load(x)
    
pkgM.__init__()
    

_dir = ''
    
running = True

logged_in = False

in_cd = False
def printLogo():
  print(color.style.RED + ''' _________   ''')                              
  print(color.style.RED + ''' \_   ___ \_______  ____   ____ '''+color.style.BLUE+'''  ____  ______''')
  print(color.style.RED + ''' /    \  \/\_  __ \/  _ \ /    \ '''+color.style.BLUE+'''/  _ \/  ___/''')
  print(color.style.RED + ''' \     \____|  | \(  <_> )   |  )'''+color.style.BLUE+'''(  <_> )___ \ ''')
  print(color.style.RED + '''  \______  /|__|   \____/|___|  /'''+color.style.BLUE+'''\____/____  >''')
  print(color.style.RED + '''         \/                   \/ '''+color.style.BLUE+'''          \/''')
  print(color.style.RESET + '\n')



def login():
  global error
  global logged_in
  global username
  global in_cd
  global _dir
  
  
  clear()
  
  load.loading()
  
  clear()
  while not logged_in:
    printLogo()
    
    username = input(' username >>')
    password = input(' password >>')
    try:
      if username == y[username]['name']:
        if password == y[username]['password']:
          logged_in = True
          ## \033[92m 
          print('logged in as '+ username)
          return
    except:
      print('Wrong Username Or Password \n')
      continue
    


  

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')
  
  
def runcd(cd_cmd):
  try:
    global in_cd
    print(os.listdir(cd_cmd))
  except:
    if cd_cmd == 'exit':
      in_cd = False
    else:
      print(color.style.BOLD + cd_cmd + color.style.RED + ' Is Not A Valid Directory')
      

def run_commands():
  global error
  global err_code
  global running
  global in_cd
  
  try:
    command_1 = command.split()[0]
    try:
      command_2 = command.split()[1]
    except:
      pass
  except:
    pass
  
  
  if command_1 == '-run':
  
    print('running '+ command_2)
    try:
       exec(open('Drive/ProgramFiles/' + command_2).read())
    except:
      print('Unable to run'+ command_2)
      err_code = 5
      return 1
    
  elif command_1 == 'exit()':
    running = False
  
  elif command_1 == 'help' or command_1 == '?':
    f = open('Drive/System/help.txt', "r")
    print(f.read())
    f.close()
    
    
  elif command_1 == 'rom':
    list = os.listdir()
    print(list)
    
  elif command_1 == 'programs':
    list = os.listdir('Drive/ProgramFiles')
    print(list)
    
  elif command_1 =='clear()':
    clear()
    printLogo()
    
  elif command_1 == 'whoami':
      print('\n')
      print(username)
      print('\n')
  
  elif command_1 == 'scan()':
    exec(open('Drive/System/AntiV.py').read())

  elif command_1 == 'cd':
    in_cd = True
    
    
  else:
      returned = pkgM.run(command_1, command)
      if returned == 11:
        global logged_in
        logged_in = False
        print('\n Logged out of ' + username + '\n')
        time.sleep(1)
        return
      elif returned == 1:
        error = 'ERR; Command Canot Be Null: exit Code 1'
        err_code = 1
        return 1
      elif returned == 2:
        return
      else:
        print('Error')


  

  
  

while running:
  
  if not logged_in:
    login()
    clear()
    printLogo()
    
    
  
  
  
  if in_cd == True:
    cd_cmd = input(color.style.BLUE + ' ~' + color.style.RESET + '$ ')

    runcd(cd_cmd)
    if in_cd == False:
      pass

  else:   
    command = input(color.style.BLUE + ' ~/'+username + color.style.RESET + '$ ')
    if run_commands() == 1:
      print(error)
  print(color.style.RESET)








