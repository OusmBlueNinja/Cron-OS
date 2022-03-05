import os, os.path, filecmp, time




class av:
  def __init__(self):
    self.token = 'xUMZJQaogb3vwmiwJqIGPo06Z'
    self.name = 'Cronso AV'
    self.files = len([name for name in os.listdir('./') if os.path.isfile(name)])

  def Clean():
    f = open('./OS.py', 'w')
    avF = open('Drive/System/Backups/code.av', 'r')
    f.write(avF.read())
    f.close()
    avF.close()
    print('cleared Viruses')

    
  def scan(self, token_check):
    if token_check == self.token:
      print('scanning', self.files, 'files')
      if filecmp.cmp('./OS.py', 'Drive/System/Backups/code.av'):
        print('No Viruses Found')
      elif not filecmp.cmp('./OS.py', 'Drive/System/Backups/code.av'):
        print('virus found')
        print('Shuting Down To Save')
        print('Please Restart')
        time.sleep(1)
        try:
          av.Clean()
        except:
          f = open('./OS.py', 'w')
          avF = open('Drive/System/Backups/code.av', 'r')
          f.write(avF.read())
          f.close()
          avF.close()
          print('cleared Viruses')
      else:
        print('error')

        

      


antiV = av()
antiV.scan('xUMZJQaogb3vwmiwJqIGPo06Z')



import os, os.path, filecmp, time




class av:
  def __init__(self):
    self.token = 'xUMZJQaogb3vwmiwJqIGPo06Z'
    self.name = 'Cronso AV'
    self.files = len([name for name in os.listdir('./') if os.path.isfile(name)])

  def Clean():
    f = open('./OS.py', 'w')
    avF = open('Drive/System/Backups/code.av', 'r')
    f.write(avF.read())
    f.close()
    avF.close()
    print('cleared Viruses')

    
  def scan(self, token_check):
    if token_check == self.token:
      print('scanning', self.files, 'files')
      if filecmp.cmp('./OS.py', 'Drive/System/Backups/code.av'):
        print('No Viruses Found')
      elif not filecmp.cmp('./OS.py', 'Drive/System/Backups/code.av'):
        print('virus found')
        print('Shuting Down To Save')
        print('Please Restart')
        time.sleep(1)
        try:
          av.Clean()
        except:
          f = open('./OS.py', 'w')
          avF = open('Drive/System/Backups/code.av', 'r')
          f.write(avF.read())
          f.close()
          avF.close()
          print('cleared Viruses')
      else:
        print('error')

        

      


antiV = av()
antiV.scan('xUMZJQaogb3vwmiwJqIGPo06Z')



