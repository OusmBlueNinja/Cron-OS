<<<<<<< HEAD
import time, json, os, sys, os.path
from Drive.System.pkg.pkg import pkgs as pkg



class pkgM_:
  def __init__(self):
    global packages
    packages = ['default']
  
  def add(new_package):
    packages.append(new_package)
  
  def run(cmd1, fullcmd, usless):
    print('trying pkg')
    try:
      return pkg.run(fullcmd)
    except:
      return
    
=======
import time, json, os, sys, os.path
from Drive.System.pkg.pkg import pkgs as pkg



class pkgM_:
  def __init__(self):
    global packages
    packages = ['default']
  
  def add(new_package):
    packages.append(new_package)
  
  def run(cmd1, fullcmd, usless):
    print('trying pkg')
    try:
      return pkg.run(fullcmd)
    except:
      return
    
>>>>>>> 53fe261 (Major Update)
pkgM = pkgM_() 